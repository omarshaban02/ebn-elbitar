from django.urls import path, include
from . import views

urlpatterns = [
    # path('',views.index, name=""),
    path('login/', include('login.urls'), name="login"),
    path('', views.home, name="home"),
    path('customerProducts/(?P<catg>[\w-]+)/', views.customerProducts, name="customerProducts"),
    path('aboutUs/', views.aboutUs, name="aboutUs"),
    path('product/(?P<product_id>[\w-]+)/', views.product, name="product"),
    path('search/', views.search, name='search_results'),
    path('order/', views.order, name='order'),
    # path('cart/(?P<customer_id>[\w-]+)/', views.cart, name='cart'),
    path('cart/', views.cart, name='cart'),
]