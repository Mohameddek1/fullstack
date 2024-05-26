from django.urls import path
from . import views

urlpatterns = [
    path("", views.course_list, name="course_list"),
    path("<int:course_id>/", views.course_detail, name="course_detail"),
    path('create_course/', views.create_course, name='create_course'),
    path('<int:course_id>/delete_course/', views.delete_course, name='delete_course'),
]