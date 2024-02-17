from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.ProductsListView.as_view()),
    path('products/', views.ProductsListView.as_view(), name='products'),
    path('categories/', views.CategoriesListView.as_view(), name='categories'),
    path('add_category/', views.AddCategoryView.as_view(), name='add_category'),
    path('add_product/', views.AddProductView.as_view(), name='add_product'),
    re_path(
        r"delete_product/(?P<pk>[0-9]+)$",
        views.DeleteProductView.as_view(),
        name='delete_product',
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)