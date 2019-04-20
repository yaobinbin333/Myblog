from django.contrib import admin
from .models import *
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "created_time", "update_time"]
    list_per_page = 7
admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag)