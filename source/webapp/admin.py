from django.contrib import admin
from webapp.models import Task, Status, Types, Project

admin.site.register(Task)
admin.site.register(Status)
admin.site.register(Types)
admin.site.register(Project)