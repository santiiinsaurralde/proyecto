from django.urls import path,include
from . import views 
from .api import ProjectViewSer
from rest_framework import routers

router= routers.DefaultRouter()
router.register('api/projects' , ProjectViewSer, 'projects')

urlpatterns = [
     path('', views.index, name="index"), 
    path('projects/', views.projects, name="projects"),
    path('projects/<int:id>', views.project_detail, name="project_detail"),
    path('create_project/', views.create_project, name="create_project"),
    path('api/projects/', include(router.urls))
]