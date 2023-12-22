from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]

data_db = [
    {'id': 1, 'title': 'Doctor 1', 'content': 'Info Doctor 1', 'is_published': True},
    {'id': 2, 'title': 'Doctor 2', 'content': 'Info Doctor 2', 'is_published': False},
    {'id': 3, 'title': 'Doctor 3', 'content': 'Info Doctor 3', 'is_published': True},
]


def about(request):
    return render(request, 'about.html', {'title': 'О сайте'})


def show_post(request, post_id):
    return HttpResponse(f"Отображение инфо доктора с id = {post_id}")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('cabinet')  # Или другой URL-адрес, на который нужно перенаправить пользователя
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


class HomeView(TemplateView):
    template_name = "home.html"


def index(request):
    return render(request, 'home.html')
