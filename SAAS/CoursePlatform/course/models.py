from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=200)  # Title of the course
    content = models.TextField()  # Description or content of the course
    created_at = models.DateTimeField(auto_now_add=True)  # Date and time when the course was created
    updated_at = models.DateTimeField(auto_now=True)  # Date and time when the course was last updated
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses_taught")  # Instructor of the course (linked to User model)
    subscribers = models.ManyToManyField(User, related_name="courses_subscribed", blank=True)  # Users subscribed to the course (many-to-many relationship with User model)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=1.99)  # Price of the course (default is 1.99)
    document = models.FileField(upload_to='docs/', default='default.pdf')  # Document associated with the course

    def __str__(self):
        return self.title  # String representation of the course is its title
