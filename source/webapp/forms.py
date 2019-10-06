from django import forms
from webapp.models import Task, Types, Status


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['created_at']


class TypesForm(forms.ModelForm):
    class Meta:
        model = Types
        fields = ['name']


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']