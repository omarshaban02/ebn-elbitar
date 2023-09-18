from django.urls import path
from . import views

urlpatterns = [
    path('',views.login, name="admin_login"),
    path('dashboard/(?P<x>[\w-]+)/',views.dashboard, name="dashboard"),
    path('customer/(?P<x>[\w-]+)/',views.customer, name="customer"),
    path('product/(?P<x>[\w-]+)/',views.product, name="product"),
    path('order/(?P<x>[\w-]+)/',views.order, name="order"),
    path('admin/(?P<x>[\w-]+)/',views.admin, name="admin"),
    path('add/(?P<x>[\w-]+)/',views.add, name="add"),
    path('show/(?P<x>[\w-]+)/(?P<y>[\w-]+)/',views.show, name="show"),
    path('profile/(?P<x>[\w-]+)/(?P<y>[\w-]+)/',views.profile, name="profile"),

]
