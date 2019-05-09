from django.contrib import admin

# Register your models here.
from acomapp.models import Category
admin.site.register(Category)

from acomapp.models import Brand
admin.site.register(Brand)

from acomapp.models import Product
admin.site.register(Product)
