from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^favicon\.ico$', RedirectView.as_view(url='static/images/favicon.ico'), name='favicon'),
    path('', views.index),
    path('infoVideo/', views.info),
    path('video/', views.creat),
    path('get/', views.chunkGet),
    path('download/', views.download)
]
