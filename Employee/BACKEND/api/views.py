from django.http import HttpResponse
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer

class ProjectViewset(viewsets.ViewSet):
    # permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    
    def get_queryset(self):
        return Project.objects.all()
    
    def list(self, request):
        """
        GET request to list all projects.
        """
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        POST request to create a new project.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """
        GET request to retrieve a single project by ID.
        """
        try:
            project = self.queryset.get(pk=pk)
            serializer = self.serializer_class(project)
            return Response(serializer.data)
        except Project.DoesNotExist:
            return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        """
        PUT request to update a single project by ID.
        """
        try:
            project = self.queryset.get(pk=pk)
        except Project.DoesNotExist:
            return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        DELETE request to delete a single project by ID.
        """
        try:
            project = self.queryset.get(pk=pk)
            project.delete()
            return Response({'message': 'Project deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Project.DoesNotExist:
            return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)
