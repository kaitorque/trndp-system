from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('empty', views.empty, name="empty"),
    path('', views.list_trndp, name="home"),
    path('list-report', views.list_report, name="list_report"),
    path('client_form', views.client_form, name="client_form"),
    path('view_report', views.view_report, name="view_report"),
    path('list-trndp', views.list_trndp, name="list_trndp"),
    path('input', views.input, name="input"),
    path('output', views.output, name="output"),
]
