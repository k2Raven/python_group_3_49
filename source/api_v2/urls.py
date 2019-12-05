from django.urls import include, path
from rest_framework import routers
from api_v2 import views

routers = routers.DefaultRouter()
routers.register(r'projects', views.ProjectViewSet)
routers.register(r'tasks', views.TaskViewSet)

app_name = 'api_v2'

urlpatterns = [
    path('', include(routers.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]