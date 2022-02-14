from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    # path('about/', views.about, name='about'),
    path('base/', views.base, name='base'),
]
