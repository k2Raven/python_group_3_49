from webapp.models import Project, Task
from rest_framework import serializers


class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'project', 'summary', 'description', 'status', 'types', 'created_at')


class ProjectSerializers(serializers.ModelSerializer):
    tasks = TaskSerializers(many=True, read_only=True, source='task')

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'created_at', 'updated_at', 'tasks')