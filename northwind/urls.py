from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.OrdersListView.as_view()),
    path('orders/', views.OrdersListView.as_view(), name='orders'),
    path('categories/', views.CategoriesListView.as_view(), name='categories'),
    path('add_category/', views.AddCategoryView.as_view(), name='add_category'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)