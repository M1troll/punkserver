from django.shortcuts import render
from . import models


def orders(request):
    orders = models.Orders.objects.all()
    return render(request, 'orders.html', {'orders': orders})


def categories(request):
    categories = models.Categories.objects.all()
    return render(request, 'categories.html', {'categories': categories})