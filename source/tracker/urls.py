"""tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import IndexView, TaskView, TaskCreateView, TaskUpdateView, TaskDeleteView,\
    StatusCreateView, TypesCreateView, StatusUpdateView, TypesUpdateView, StatusDeleteView, TypesDeleteView,\
    ProjectView, ProjectListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProjectListView.as_view(), name='project_list'),
    path('project/<int:pk>', ProjectView.as_view(), name='project_view'),
    path('task/', IndexView.as_view(), name='index'),
    path('task/<int:pk>', TaskView.as_view(), name='task_view'),
    path('task/add/', TaskCreateView.as_view(), name='task_add'),
    path('status/add/', StatusCreateView.as_view(), name='status_add'),
    path('types/add/', TypesCreateView.as_view(), name='types_add'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_update'),
    path('status/<int:pk>/edit/', StatusUpdateView.as_view(), name='status_update'),
    path('types/<int:pk>/edit/', TypesUpdateView.as_view(), name='types_update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='delete_task'),
    path('status/<int:pk>/delete/', StatusDeleteView.as_view(), name='delete_status'),
    path('types/<int:pk>/delete/', TypesDeleteView.as_view(), name='delete_types')
]
