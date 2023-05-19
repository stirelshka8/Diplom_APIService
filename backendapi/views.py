from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def first_page(request):
    return HttpResponse("API Сервис заказа товаров для розничных сетей")
