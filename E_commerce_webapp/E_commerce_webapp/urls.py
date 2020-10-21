from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from apps.core.views import frontpage, contactpage

urlpatterns = [

    url(r'^accounts/', include('accounts.urls')),
    path('', frontpage, name="frontpage"),
    path('contact/', contactpage , name="contact"),
    path('admin/', admin.site.urls),
]
