from django.contrib import admin

# Register your models here.
# project/admin.py
from .models import product

admin.site.register(product)
