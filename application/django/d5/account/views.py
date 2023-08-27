from django.shortcuts import render
from django.shortcuts import redirect

from .forms import AccountForm


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
        account_form = AccountForm()
        return render(request, 'sign-in.html', dict(form=account_form))
