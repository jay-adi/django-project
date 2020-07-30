from django.contrib import admin
from . models import Product,upi
from django.contrib.auth.models import Group

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    #list_display = ('description', 'image_tag')

        list_display = ('name', 'address','height','weight', 'trek','confirm','price','id_proof')
        list_filter = ('trek', 'confirm',)
admin.site.register(Product,ProductAdmin)
#admin.site.register(Location1,ProductAdmin)
#fields = ['image_tag']
#readonly_fields = ['image_tag']
admin.site.unregister(Group)
admin.site.site_header="CLIFF CAT ADMIN"
admin.site.register(upi)