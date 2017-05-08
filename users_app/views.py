# coding=utf-8
import threading
from datetime import datetime
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, render_to_response
from django.contrib.auth.views import logout
from django.template import loader
from django.urls import reverse

from categories.views import generate_view_params
from .forms import LoginForm, RegisterForm, SetPasswordForm
from .models import Users
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from Classified.parameters import SITE_PROTOCOL, SITE_URL


# Create your views here.


def users_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def users_login(request):
    login_form = LoginForm(request.POST)
    if request.POST:
        if login_form.is_valid():
            email = login_form.cleaned_data.get('email')
            password = login_form.cleaned_data.get('password')

            if email and password:
                user = authenticate(email=email, password=password)
                if user is None:
                    return JsonResponse(dict(success=False, message='Неправильный логин или пароль'))
                else:
                    if not user.is_active:
                        return JsonResponse(dict(success=False, message='Ваш аккаунт был заблокирован'))
                    else:
                        login(request, user)
                        return JsonResponse(dict(success=True, message='login'))
        else:
            return JsonResponse(dict(success=False, message=str(login_form.errors)))
    return JsonResponse(dict(success=False, message='Запрос должен быть POST'))


def users_register(request):
    register_form = RegisterForm(request.POST)
    if request.POST:
        if register_form.is_valid():
            email = register_form.cleaned_data['email']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            try:
                user = Users.objects.get(email=email)
                return JsonResponse(dict(
                    success=False,
                    message='Этот пользователь уже существует. Пользователь зарегистрирован %s' % str(user.date_joined)
                ))
            except ObjectDoesNotExist:
                if password1 and password2 and password1 == password2:
                    user = Users(
                        email=email,
                        password=make_password(password1),
                        date_joined=datetime.now(),
                        is_active=True,
                        is_staff=True
                    )
                    user.save()
                    token = default_token_generator.make_token(user)
                    uid = urlsafe_base64_encode(force_bytes(user.pk))
                    _password = urlsafe_base64_encode(password1)

                    template = loader.get_template('app/partial/confirm_email.html')
                    contexts = {
                        'link': SITE_PROTOCOL + SITE_URL + reverse('users:users_confirm',
                                                                   kwargs={'uidb64': uid, 'token': token,
                                                                           'password': _password})
                    }
                    print contexts
                    response = template.render(contexts, request)
                    thread = threading.Thread(
                        target=user.email_user,
                        args=(
                            u'Активация пользователя | TumaR24',
                            response
                        )
                    )
                    thread.start()
                    return JsonResponse(dict(
                        success=True,
                        message='register'
                    ))
        else:
            return JsonResponse(dict(success=False, message=str(register_form.errors)))
    return JsonResponse(dict(success=False, message='Запрос должен быть POST'))


email_confirm_messages = {
    'inactive': 'inactive_error',
    'invalid': 'invalid_user_data',
    'does_not_exists': 'user_does_not_exists',
    'invalid_data': 'invalid_token_or_uidb64',
    'deprecated_token': 'deprecated_user_token'
}


def users_email_confirm(request, uidb64, token, password):
    if uidb64 is not None and token is not None:
        uid = urlsafe_base64_decode(uidb64)
        password = urlsafe_base64_decode(password)
        try:
            user = Users.objects.get(pk=uid)
            if user.email_token != token:
                if default_token_generator.check_token(user, token):
                    user_cache = authenticate(email=user.email, password=password)
                    if user_cache is not None:
                        if user_cache.is_active:
                            login(request, user_cache)
                            user.email_token = token
                            user.save()

                            return HttpResponseRedirect(
                                reverse('users:users_confirm_result', kwargs={'success': True})
                            )
                        else:
                            return HttpResponseRedirect(
                                reverse('users:users_confirm_result', kwargs={'success': False}) + '?message=' +
                                email_confirm_messages['inactive']
                            )
                    return HttpResponseRedirect(
                        reverse('users:users_confirm_result', kwargs={'success': False}) + '?message=' +
                        email_confirm_messages['invalid']
                    )
            return HttpResponseRedirect(
                reverse('users:users_confirm_result', kwargs={'success': False}) + '?message=' +
                email_confirm_messages['deprecated_token']
            )
        except ObjectDoesNotExist:
            return HttpResponseRedirect(
                reverse('users:users_confirm_result', kwargs={'success': False}) + '?message=' + email_confirm_messages[
                    'does_not_exists']
            )
    return HttpResponseRedirect(
        reverse('users:users_confirm_result', kwargs={'success': False}) + '?message=' + email_confirm_messages[
            'invalid_data']
    )


def users_email_confirm_result(request, success):
    params = dict()
    params.update(generate_view_params(request))
    if success == 'True':
        params['success'] = True
    else:
        message = request.GET.get('message')
        temp_params = {
            'success': False
        }
        if message == email_confirm_messages['inactive']:
            temp_params['message'] = u'Ваш пользователь был заблокирован<br>Обратитесь к администраторам: ' \
                                     u'<a href="mailto:okay11007@gmail.com">Okay11007@gmail.com</a>'
            temp_params['reason'] = 'inactive'
        if message == email_confirm_messages['invalid']:
            temp_params['message'] = u'Мы не смогли вас авторизовать, пожалуйста авторизуйтесь'
            temp_params['form'] = LoginForm
            temp_params['reason'] = 'invalid'
        if message == email_confirm_messages['does_not_exists']:
            temp_params['message'] = u'Мы не смогли найти этого пользователя, попробуйте зарегистрироваться заново'
            temp_params['form'] = RegisterForm
            temp_params['reason'] = 'does_not_exists'
        if message == email_confirm_messages['invalid_data']:
            temp_params['message'] = u'Данные для активации аккаунта неправильные'
            temp_params['reason'] = 'invalid_data'
        if message == email_confirm_messages['deprecated_token']:
            temp_params['message'] = u'Ссылка на активацию вашего аккаунта устарела'
            temp_params['reason'] = 'deprecated_token'
        params.update(temp_params)

    return render(request, 'app/email_verify.html', params)


@login_required
def set_user_password(request):
    form = SetPasswordForm(request.POST)
    params = {
        'set_password_form': form
    }
    if request.POST:
        if form.is_valid():
            pass1 = form.cleaned_data['password1']
            pass2 = form.cleaned_data['password2']

            if pass1 and pass2 and pass1 == pass2:
                try:
                    current_user = Users.objects.get(email=request.user.email)
                    current_user.password = make_password(pass1)
                    current_user.save()
                    user = authenticate(email=current_user.email, password=pass1)
                    login(request, user)
                    params.update(dict(result=True, message='Ваш пароль успешно изменен!'))
                except ObjectDoesNotExist:
                    params.update(dict(result=False, message='Мы не нашли пользователя'))
            else:
                params.update(dict(result=False, message='Пароли не сопадают'))
    print params
    params.update(generate_view_params(request))
    return render(request, 'app/partial/set_password.html', params)
