from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from api_v2 import views

routers = routers.DefaultRouter()
routers.register(r'projects', views.ProjectViewSet)
routers.register(r'tasks', views.TaskViewSet)

app_name = 'api_v2'

urlpatterns = [
    path('', include(routers.urls)),
    path('login/', obtain_auth_token, name='api_token_auth')
]