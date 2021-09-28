from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from rest_framework.decorators import api_view

# permission_classes,

from rest_framework.response import Response

# from rest_framework.permissions import IsAuthenticated
from .serializers import TaskSerializer

from rest_framework import status

from todo.models import Task

# Create your views here.


@api_view(["GET"])
def apiOverview(request):
    """Overview of the whole api urls
    """
    api_urls = {
        "Login": "/accounts/api/login",
        "Register": "/accounts/api/register",
        "List": "/task-list/",
        "Detail": "/api/task-detail/<str:pk>/",
        "Create": "/api/task-create/",
        "Update": "/api/task-update/<str:pk>/",
        "Delete": "/api/task-delete/<str:pk>/",
    }

    return Response(api_urls)


# @permission_classes((IsAuthenticated, ))
@api_view(["GET", "POST"])
def taskList(request):
    """
    ---
    response_serializer: TaskSerializer
    parameters:
            - title: CharField

    """
    if request.method == "GET":
        tasks = Task.objects.all().order_by("-id")
        serializers = TaskSerializer(tasks, many=True)
        return Response(serializers.data)
    elif request.method == "POST":
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            # building_serializer.validated_data['user'] = request.user
            serializer.save()
            return JsonResponse(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return JsonResponse(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


# @permission_classes((IsAuthenticated, ))


@api_view(["GET", "POST", "DELETE"])
def taskDetail(request, pk):
    task = get_object_or_404(Task, id=pk)  # user=request.user,
    if request.method == "GET":
        serializers = TaskSerializer(task, many=False)
        return Response(serializers.data)
    elif request.method == "POST":
        serializer = TaskSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
    elif request.method == "DELETE":
        task.delete()
        return JsonResponse({"detail": "Task was deleted successfully!"})
