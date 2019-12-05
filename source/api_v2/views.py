from rest_framework import viewsets
from webapp.models import Project, Task
from api_v2.serializers import ProjectSerializers, TaskSerializers


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
