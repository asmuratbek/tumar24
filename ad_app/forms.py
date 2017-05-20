# coding=utf-8
from django import forms
from django.urls import reverse

from .models import Ad
from app.models import City, Metro
from categories.models import Category


class SearchForm(forms.Form):
    search_word = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'type': 'search',
        'placeholder': 'Поиск по объявлениям...'
    }), required=False)
    city = forms.ChoiceField(widget=forms.Select(attrs={'class': 'city-choice', 'id': 'search_city'}), required=False)
    metro = forms.CharField(widget=forms.Select(), required=False)
    categories = forms.ChoiceField(widget=forms.Select(), required=False)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)

        city_choices = (('', 'Город'),)
        for item in City.objects.all():
            city_choices += ((str(item.id), item.title),)

        category_choices = (('', 'Категория'),)
        for item in Category.objects.filter(parent=None):
            category_choices += ((str(item.id), item.title),)
            for sub in Category.objects.filter(parent=item):
                category_choices += ((str(sub.id), '--' + sub.title),)

        self.fields['categories'].choices = category_choices
        self.fields['city'].choices = city_choices
        self.fields['city'].widget.attrs.update({'data-url': reverse('get_metro_by_city')})
        self.fields['metro'].widget.choices = (('', 'Метро'), ('', 'Выберите город'))


class AdCreationForm(forms.ModelForm):
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    location = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = Ad
        fields = ('category', 'metro', 'title', 'price', 'city', 'description', 'phone')

    def __init__(self, *args, **kwargs):
        super(AdCreationForm, self).__init__(*args, **kwargs)

        category_choices = (('', 'Выберите категорию'),)
        for item in Category.objects.filter(parent=None):
            category_choices += ((str(item.id), item.title),)
            for sub in Category.objects.filter(parent=item):
                category_choices += ((str(sub.id), '--' + sub.title),)

        metro_choices = (('', 'Метро'), ('', 'Выберите сначала город'),)

        city_choices = (('', 'Выберите город'),)
        for item in City.objects.all():
            city_choices += ((str(item.id), item.title),)

        self.fields['category'].choices = category_choices
        self.fields['metro'].choices = metro_choices
        self.fields['city'].choices = city_choices
        self.fields['city'].widget.attrs.update({'class': 'city-choice', 'data-url': reverse('get_metro_by_city'), 'id': 'ad_creation_city'})
