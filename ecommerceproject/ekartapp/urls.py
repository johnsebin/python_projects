
from django.urls import path
from . import views
from ecommerceproject import settings
app_name='ekartapp'
urlpatterns = [

    path('', views.allProdcat, name='allProdCat'),
    path('products/<slug:c_slug>/', views.allProdcat, name='products_by_category'),
    path('products/<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatdetail'),
]