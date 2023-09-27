from django.contrib import admin
from .models import Catagory,Product,OrderDetails
# Register your models here.
admin.site.register(Catagory)
admin.site.register(Product)

class OrderAdmin(admin.ModelAdmin):
    list_display=['username','email','Medicine_name','quantity','price']

admin.site.register(OrderDetails,OrderAdmin)


