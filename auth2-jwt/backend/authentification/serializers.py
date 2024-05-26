from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Specifies the model to be serialized/deserialized
        fields = ['id', 'username', 'password']  # Specifies the fields to include in the serialized representation
        extra_kwargs = {"password": {"write_only": True}}  # Specifies additional options for specific fields

    def create(self, validated_data):
        """
        Method to create a new user based on validated data.
        """
        user = User.objects.create_user(**validated_data)  # Creates a new user using the provided validated data
        return user  # Returns the created user object


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at', 'author']
        extra_kwargs = {"author": {"read_only": True}}
        





