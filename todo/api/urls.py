from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path("", views.apiOverview, name="api-overview"),
    path("task-list/", views.taskList, name="task-list"),
    path("task-create/", views.taskList, name="task-create"),
    path("task-detail/<str:pk>/", views.taskDetail, name="task-detail"),
    path("task-update/<str:pk>/", views.taskDetail, name="task-update"),
    path("task-delete/<str:pk>/", views.taskDetail, name="task-delete"),    
]
