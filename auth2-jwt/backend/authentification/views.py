from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

# Create your views here.

class NoteListCreate(generics.ListCreateAPIView):
    """
    A view for listing and creating notes.
    """
    serializer_class = NoteSerializer  # Specifies the serializer class to use for serializing/deserializing notes
    permission_classes = [IsAuthenticated]  # Specifies the permission classes required for accessing this view

    def get_queryset(self):
        """
        Method to retrieve the queryset of notes.
        """
        user = self.request.user  # Retrieves the authenticated user making the request
        return Note.objects.filter(author=user)  # Filters notes based on the authenticated user

    def perform_create(self, serializer):
        """
        Method to perform custom actions when creating a new note.
        """
        if serializer.is_valid():
            serializer.save(author=self.request.user)  # Sets the author of the note to the authenticated user
        else:
            print(serializer.errors)  # Prints validation errors if the serializer is not valid
    


class NoteDelete(generics.DestroyAPIView):
    """
    A view for deleting notes.
    """
    serializer_class = NoteSerializer  # Specifies the serializer class to use for serializing/deserializing notes
    permission_classes = [IsAuthenticated]  # Specifies the permission classes required for accessing this view

    def get_queryset(self):
        """
        Method to retrieve the queryset of notes.
        """
        user = self.request.user  # Retrieves the authenticated user making the request
        return Note.objects.filter(author=user)  # Filters notes based on the authenticated user

class CreateUserView(generics.CreateAPIView):
    """
    A view for creating users.
    """
    queryset = User.objects.all()  # Queryset for retrieving existing users
    serializer_class = UserSerializer  # Serializer class for serializing/deserializing user data
    permission_classes = [AllowAny]  # Permissions required for accessing this view




































