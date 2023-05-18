from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_page, name='API Documentation'),
    path('api/v1/', views.first_page, name='API Documentation')
]
