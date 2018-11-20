from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('order/send', views.order, name='order'),
    path('success', views.success, name='order'),
]