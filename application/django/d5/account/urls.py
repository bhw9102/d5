from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('empty', views.empty, name='empty'),
    path('sign-in', views.sign_in, name='sign_in'),
    path('sign-out', views.sign_out, name='sign_out'),
]