from django.views.generic import ListView
from django.views.generic.edit import CreateView
from . import models
from django.urls import reverse_lazy
from django.db.models import Q 


class ProductsListView(ListView):
    """Render table of products."""
    model = models.Products
    template_name = "products.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_products"] = True
        context["add_link"] = "add_product"
        return context

    def get_queryset(self):
        query = self.request.GET.get("search")

        if not query:
            return super().get_queryset()

        object_list = models.Products.objects.filter(
            Q(category__category_id=query)
            | Q(product_name__contains=query)
            | Q(units_in_stock=query)
        )
        return object_list


class CategoriesListView(ListView):
    """Render table of categories."""
    model = models.Categories
    template_name = "categories.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_categories"] = True
        context["add_link"] = "add_category"
        return context

    def get_queryset(self):
        query = self.request.GET.get("search")

        if not query:
            return super().get_queryset()

        object_list = models.Categories.objects.filter(
            Q(category_id__icontains=query)
            | Q(category_name__icontains=query)
            | Q(description__icontains=query)
        )
        return object_list


class AddCategoryView(CreateView):
    model = models.Categories
    template_name = "add_category.html"
    fields = ["category_name", "description"]

    success_url = reverse_lazy("categories")


class AddProductView(CreateView):
    model = models.Products
    template_name = "add_product.html"
    fields = [
        "product_name",
        "supplier",
        "category",
        "quantity_per_unit",
        "unit_price",
        "units_in_stock",
        "units_on_order",
        "reorder_level",
        "discontinued",
    ]

    success_url = reverse_lazy("products")
