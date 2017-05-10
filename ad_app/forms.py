# coding=utf-8
from django import forms
from .models import Ad
from app.models import City, Metro
from categories.models import Category


class SearchForm(forms.Form):
    search_word = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'type': 'search',
        'placeholder': 'Поиск по объявлениям...'
    }))
    metro = forms.ChoiceField(widget=forms.Select(), required=False)
    categories = forms.ChoiceField(widget=forms.Select(), required=False)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)

        category_choices = (('', 'Категория'),)
        for item in Category.objects.all():
            category_choices += ((str(item.id), item.title),)

        metro_choices = (('', 'Метро'),)
        for item in Metro.objects.all():
            metro_choices += ((str(item.id), item.title),)

        self.fields['metro'].choices = metro_choices
        self.fields['categories'].choices = category_choices


class AdCreationForm(forms.ModelForm):
    images = forms.ImageField(allow_empty_file=True, required=False)
    location = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = Ad
        fields = ('category', 'metro', 'title', 'price', 'city', 'description', 'phone')

    def __init__(self, *args, **kwargs):
        super(AdCreationForm, self).__init__(*args, **kwargs)

        category_choices = (('', 'Выберите категорию'),)
        for item in Category.objects.all():
            category_choices += ((str(item.id), item.title),)

        metro_choices = (('', 'Выберите станцию метро'),)
        for item in Metro.objects.all():
            metro_choices += ((str(item.id), item.title),)

        city_choices = (('', 'Выберите город'),)
        for item in City.objects.all():
            city_choices += ((str(item.id), item.title),)

        self.fields['category'].choices = category_choices
        self.fields['metro'].choices = metro_choices
        self.fields['city'].choices = city_choices
