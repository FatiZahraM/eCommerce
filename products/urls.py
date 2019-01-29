
from django.urls import path
from .import views


app_name = 'products'

urlpatterns = [
    path('', views.all, name='all_products'),
    path('<slug>/', views.single, name='single_product'),
    path('search/', views.search, name='search'),
]
