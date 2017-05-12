from django.shortcuts import render
from categories.views import generate_view_params

# Create your views here.


def page_not_found(request):
    params = {

    }
    params.update(generate_view_params(request))
    return render(request, 'exceptions/not_found.html', params)
