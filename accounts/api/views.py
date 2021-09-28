from rest_framework.decorators import api_view
from .serializers import LoginSerializer, RegisterSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from django.http import JsonResponse


@api_view(["POST"])
def loginView(request, format=None):
    serializer = LoginSerializer(data=request.data, many=False)

    if serializer.is_valid():
        user = serializer.validated_data.get("user")
        if user is not None and user.is_active:
            login(request, user)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def logoutView(request, format=None):
    logout(request)
    return JsonResponse(
        {"non_field_errors": "successfully logged out"},
        status=status.HTTP_200_OK,
    )


@api_view(["POST"])
def registerView(request, format=None):

    serializer = RegisterSerializer(data=request.data, many=False)

    if serializer.is_valid():
        username = serializer.validated_data["username"]
        password = serializer.validated_data["password1"]
        user = User.objects.create_user(username=username, password=password)
        authenticate(request, username=username, password=password)
        login(request, user)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
