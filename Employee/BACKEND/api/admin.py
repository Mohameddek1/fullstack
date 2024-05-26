from django.contrib import admin
from .models import *

# Register your models here.
class projectAdmin(admin.ModelAdmin):
    list_display = ("name", "start_date", "end_date", "comments", "status")
admin.site.register(Project)