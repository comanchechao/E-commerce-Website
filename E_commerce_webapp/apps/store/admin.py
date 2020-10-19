from django.contrib import admin

# Register your models here.
from .models import Catagory , Product

admin.site.register(Catagory)
admin.site.register(Product)