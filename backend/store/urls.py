from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.store, name='store'),
    path('<slug:slug>/', views.detail, name='detail'),
]