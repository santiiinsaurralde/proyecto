from .models import Project
from rest_framework import viewsets, permissions
from .rest import myappApi

class ProjectViewSer(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = myappApi