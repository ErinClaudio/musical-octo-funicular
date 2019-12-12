from django.urls import path
from projects import views

app_name = 'projects'

urlpatterns = [
    path('', views.all_projects1, name = 'all_projects1') #,
    #path('<int:pk>' , views.project_detail, name='project_detail')
    ]