from django.contrib import admin
from .models import *

# Register your models here.


class AdminOrder(admin.ModelAdmin):
    list_display = ['room_id','room_status']


admin.site.register(Maneeger)
admin.site.register(Category)
admin.site.register(Rooms,AdminOrder)
admin.site.register(UserDetails)
admin.site.register(EmplyeeCategory)
admin.site.register(Emplyee)
