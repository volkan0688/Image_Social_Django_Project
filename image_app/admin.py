from django.contrib import admin
from image_app.models import Image
# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    fields = ['nickname','image','message']


admin.site.register(Image,ImageAdmin)
