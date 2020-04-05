from django.urls import path, include
from .views import Home, ProductListView

urlpatterns = [
    path('', Home, name='home'),
    path('products/', ProductListView, name='products'),
]
