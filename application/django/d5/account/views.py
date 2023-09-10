from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login

from .forms import SignInForm


def index(request):
    if request.method != "GET":
        raise Exception()
    if request.user.is_authenticated:
        return redirect('empty')
    return redirect('sign_in')


def empty(request):
    if not request.user.is_authenticated:
        return redirect('index')
    return render(request, 'empty.html')


def sign_in(request):
    if request.method == "GET":
        sign_in_form = SignInForm()
        return render(request, 'sign-in.html', dict(form=sign_in_form))
    sign_in_form = SignInForm(request.POST)
    if not sign_in_form.is_valid():
        return render(request, 'sign-in.html', dict(form=sign_in_form))
    username = sign_in_form.cleaned_data.get('email')
    password = sign_in_form.cleaned_data.get('password')
    user = authenticate(username=username, password=password)
    if not user:
        return render(request, 'sign-in.html', dict(form=sign_in_form))
    login(request, user)
    return redirect('index')

