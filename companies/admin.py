from django.contrib import admin

# Register your models here.
from .models import Stock
from .models import Users
from .models import Subcategory,Sku,Subcategory_SKU
admin.site.register(Stock)
admin.site.register(Users)
admin.site.register(Subcategory)
admin.site.register(Sku)
admin.site.register(Subcategory_SKU)

