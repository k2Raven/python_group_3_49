from django.contrib import admin
from webapp.models import Task, Status, Types

admin.site.register(Task)
admin.site.register(Status)
admin.site.register(Types)