from django.contrib import admin
from django.urls import path

from apps.core.views import frontpage, contactpage

urlpatterns = [
    path('', frontpage, name="frontpage"),
    path('contact/', contactpage , name="contact"),
    path('admin/', admin.site.urls),
]
