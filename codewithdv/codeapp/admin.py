from django.contrib import admin
from codeapp.models import *
# Register your models here.

class showourgallery(admin.ModelAdmin):
    list_display = ["c_name", "c_pic", "c_id", "c_createddate", "c_type", "c_fullcode", "c_required", "c_des"]
admin.site.register(ourgallery, showourgallery)

class showcategory(admin.ModelAdmin):
    list_display = ["cat_name"]
admin.site.register(category, showcategory)


class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "msg")
admin.site.register(contact, ContactAdmin)