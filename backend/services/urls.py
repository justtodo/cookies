from django.urls import path

from . import views

app_name = 'services'

urlpatterns = [
    path('', views.services, name='services'),
    path('item/<slug:slug>/', views.details, name='details'),
    path('experts/', views.experts, name='experts'),
    path('experts/<slug:slug>/', views.details_experts, name='details_experts'),
]