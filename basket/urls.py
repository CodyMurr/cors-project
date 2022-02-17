from django.urls import path
from . import views

app_name = 'basket'

urlpatterns = [
    path('', views.basket_summary, name='basket_summary'),
    path('add/<int:id>/', views.basket_add, name='basket_add'),
    path('item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('basket_clear/', views.basket_clear, name='basket_clear'),
    path('basket_detail/', views.basket_detail, name='basket_detail'),
]
