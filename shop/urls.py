from django import urls
from . import views
from django.urls import path


app_name = 'shop'

urlpatterns = [
    path('', views.wine_list, name='wine_list'),
    path('<slug:category_slug>', views.wine_list, name='wine_list_by_category'),
    path('<int:id>/<slug:slug>/', views.wine_detail, name='wine_detail')
]
