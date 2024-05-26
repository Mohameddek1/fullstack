from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["title", "instructor", "created_at", "updated_at"]  # Fields to display in the list view of Course model
    search_fields = ["title", "instructor__username"]  # Fields to search by in the admin interface
    list_filter = ["created_at", "updated_at", "instructor"]  # Fields to filter by in the admin interface
