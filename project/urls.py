from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('homepage',views.homepage,name='homepage'),
    path('add-product/', views.add_product, name='add_product')
]
