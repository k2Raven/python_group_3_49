from django import forms
from webapp.models import Task, Types, Status, Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['created_at', 'updated_at']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['created_at', 'project']


class TypesForm(forms.ModelForm):
    class Meta:
        model = Types
        fields = ['name']


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']