from django.shortcuts import render
from categories.views import get_categories, generate_view_params
# Create your views here.


def index(request):
    params = {

    }
    params.update(generate_view_params(request))
    print params
    return render(request, 'app/index.html', params)
