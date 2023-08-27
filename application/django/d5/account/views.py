from django.shortcuts import render
from django.shortcuts import redirect

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
    sign_in_form = SignInForm(request)
    if not sign_in_form.is_valid():
        return render(request, 'sign-in.html', dict(form=sign_in_form))
    request.session['user'] = ''
    return redirect('index')

