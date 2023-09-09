from django.contrib import admin
from .models import *

# Register your models here.
class imageAdmin(admin.ModelAdmin):
    list_display = ["room", "img_tag", "images"] # new
admin.site.register(Room)
admin.site.register(owner_details)
admin.site.register(room_images,imageAdmin)
# admin.site.register(model_form_single)
