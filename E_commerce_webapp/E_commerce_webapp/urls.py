from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from apps.core.views import *
from apps.store.views import *
from apps.cart.views import *

urlpatterns = [

    url(r'^accounts/', include('accounts.urls')),
    path('', frontpage, name="frontpage"),
    path('cart/' , cart , name="cart"),
    path('contact/', contactpage , name="contact"),
    path('about/', aboutspage, name="abouts"),
    path('<slug:category_slug>/<slug:slug>', product_detail, name="product_detail"),
    path('<slug:slug>', category_detail, name="category_detail"),
    path('admin/', admin.site.urls),
]
