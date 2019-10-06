from django.contrib import admin
from .models import Uploader,Uploads,tags

# Register your models here.
class UploadsAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

admin.site.register(Uploader)
admin.site.register(Uploads)
admin.site.register(tags)
