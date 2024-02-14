from django.shortcuts import render


def orders(request):
    return render(request, 'orders.html')


def categories(request):
    return render(request, 'categories.html')