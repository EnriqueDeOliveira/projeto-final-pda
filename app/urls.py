from django.urls import path

from app import views

urlpatterns = [
    path('',views.index),
    path('sobre/',views.sobre),
    path('contato/',views.contato),
    path('login/',views.login),
    path('cadastro/',views.cadastro)
]