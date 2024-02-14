from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.orders),
    path('orders/', views.orders, name='orders'),
    path('categories/', views.categories, name='categories'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)