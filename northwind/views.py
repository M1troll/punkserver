from django.views.generic import ListView
from django.views.generic.edit import CreateView
from . import models


class OrdersListView(ListView):
    """Render table of orders."""
    model = models.Orders
    template_name = "orders.html"


class CategoriesListView(ListView):
    """Render table of categories."""
    model = models.Categories
    template_name = "categories.html"


class AddCategoryView(CreateView):
    model = models.Categories
    template_name = "add_category.html"
    fields = ["category_name", "description"]
    # , "picture"]
