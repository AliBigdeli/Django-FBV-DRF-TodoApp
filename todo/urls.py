from django.urls import path, include
from . import views

app_name = "todo"

urlpatterns = [
    path("", views.indexView, name="list2"),
    path("api/", include("todo.api.urls")),
]
