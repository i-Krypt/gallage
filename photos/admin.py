from django.contrib import admin
from .models import Uploader,Uploads,tags

# Register your models here.
admin.site.register(Uploader)
admin.site.register(Uploads)
admin.site.register(tags)
