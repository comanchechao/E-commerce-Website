from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from apps.core.views import frontpage, contactpage
from apps.store.views import product_detail, category_detail

urlpatterns = [

    url(r'^accounts/', include('accounts.urls')),
    path('', frontpage, name="frontpage"),
    path('contact/', contactpage , name="contact"),
    path('<slug:category_slug>/<slug:slug>', product_detail, name="product_detail"),
    path('<slug:slug>', category_detail, name="category_detail"),
    path('admin/', admin.site.urls),
]
