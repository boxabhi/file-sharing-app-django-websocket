from django.contrib import admin

# Register your models here.
from .models import Folder,Files


admin.site.register(Files)
admin.site.register(Folder)
