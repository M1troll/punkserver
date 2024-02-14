from django.shortcuts import render
from . import models


def orders(request):
    orders = models.Orders.objects.all()
    return render(request, 'orders.html', {'orders': orders})


def categories(request):
    categories = models.Categories.objects.all()
    import ipdb; ipdb.set_trace()
    from io import BytesIO
    a3 = bytes.fromhex(categories[0].picture)
    return render(request, 'categories.html', {'categories': categories})