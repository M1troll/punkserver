from django.views.generic import ListView, CreateView, DeleteView
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
        units = self.request.GET.get("units_in_stock")
        condition = self.request.GET.get("condition", "")

        if query and not units:
            return models.Products.objects.filter(self._get_search_conditions(query))

        if units and not query:
            conditions = Q(units_in_stock=units)
            if condition:
                conditions = self._get_units_conditions(condition, units)
            return models.Products.objects.filter(conditions)
       
        if query and units:
            conditions = self._get_search_conditions(query) | Q(units_in_stock=units)
            return models.Products.objects.filter(conditions)
       
        if query and units:
            return models.Products.objects.filter(
                self._get_search_conditions(query)
                | self._get_units_conditions(condition, units)
            )
        
        return super().get_queryset()

    def _get_search_conditions(self, query: str | int) -> Q:
        conditions = Q(product_name__contains=query)
        try:
            category_id = int(query)
            conditions = conditions | Q(category__category_id=category_id)
        except:
            pass
        return conditions
    
    def _get_units_conditions(self, condition: str, units: str) -> Q:
        if condition == ">":
            conditions = Q(units_in_stock__gte=units)
        elif condition == "<":
            conditions = Q(units_in_stock__lt=units)
        else: 
            conditions = Q(units_in_stock=units)
        return conditions




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


class DeleteProductView(DeleteView):
    model = models.Products
    template_name = "delete_category.html"
    success_url = reverse_lazy("products")
