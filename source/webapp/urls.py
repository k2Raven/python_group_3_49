from django.urls import path
from webapp.views import IndexView, TaskView, TaskCreateView, TaskUpdateView, TaskDeleteView,\
    StatusCreateView, TypesCreateView, StatusUpdateView, TypesUpdateView, StatusDeleteView, TypesDeleteView,\
    ProjectView, ProjectListView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project_view'),
    path('project/add/', ProjectCreateView.as_view(), name='project_add'),
    path('project/<int:pk>/edit/', ProjectUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='delete_project'),
    path('task/', IndexView.as_view(), name='index'),
    path('task/<int:pk>/', TaskView.as_view(), name='task_view'),
    path('project/<int:pk>/add-task/', TaskCreateView.as_view(), name='task_add'),
    path('status/add/', StatusCreateView.as_view(), name='status_add'),
    path('types/add/', TypesCreateView.as_view(), name='types_add'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_update'),
    path('status/<int:pk>/edit/', StatusUpdateView.as_view(), name='status_update'),
    path('types/<int:pk>/edit/', TypesUpdateView.as_view(), name='types_update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='delete_task'),
    path('status/<int:pk>/delete/', StatusDeleteView.as_view(), name='delete_status'),
    path('types/<int:pk>/delete/', TypesDeleteView.as_view(), name='delete_types')
]