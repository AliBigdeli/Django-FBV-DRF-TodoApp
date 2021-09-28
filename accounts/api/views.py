from django.shortcuts import redirect
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from .serializers import LoginSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from django.http import JsonResponse


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
def loginView(request, format=None):

    serializer = LoginSerializer(data=request.data, many=False)

    if serializer.is_valid():
        user = serializer._validated_data.get("user")
        if user is not None and user.is_active:
            login(request, user)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    return JsonResponse(
        serializer.errors, status=status.HTTP_400_BAD_REQUEST
    )

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
def logoutView(request, format=None):
    logout(request)
    return JsonResponse({"non_field_errors":"successfully logged out"}, status=status.HTTP_200_OK)

