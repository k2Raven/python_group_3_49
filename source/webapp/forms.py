from django import forms
from django.forms import widgets

from webapp.models import Types, Status


class TaskForm(forms.Form):
    summary = forms.CharField(max_length=200, required=True, label='Краткое описание')
    description = forms.CharField(max_length=3000, required=False, label='Полное описание',
                                  widget=widgets.Textarea)
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=True, label='Статус', empty_label=None)
    types = forms.ModelChoiceField(queryset=Types.objects.all(), required=True, label='Тип', empty_label=None)
