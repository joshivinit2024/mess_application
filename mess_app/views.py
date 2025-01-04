from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
import csv
import json
from django.http import HttpResponse
from django.shortcuts import render
import io
from rest_framework.decorators import api_view, permission_classes,parser_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout
from django.contrib.auth.hashers import check_password
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password
from .models import User,Details 
from .serializers import UserSerializer,DetailsSerializer
from rest_framework.pagination import PageNumberPagination

@api_view(['POST'])
def signup(request):
    data = request.data
    data['password'] = make_password(data['password'])
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'User created successfully'}, status=201)
    return Response(serializer.errors, status=400)

# @api_view(['POST'])
# def login(request):
#     data = request.data
#     try:
#         user = User.objects.get(email=data['email'])
#         number=User.objects.get(email=data['email'])
#         if check_password(data['password'], user.password):
#             return Response({'message': 'Login successful', 'user_id': user.user_id,'number':number.number}, status=200)
#         return Response({'message': 'Invalid credentials'}, status=400)
#     except User.DoesNotExist:
#         return Response({'message': 'Invalid credentials'}, status=400)

@api_view(['POST'])
def login(request):
    data = request.data
    try:
        user = User.objects.get(number=data['number'])
        if check_password(data['password'], user.password):
            return Response({'message': 'Login successful', 'user_id': user.user_id, 'number': user.number}, status=200)
        return Response({'message': 'Invalid credentials'}, status=400)
    except User.DoesNotExist:
        return Response({'message': 'Invalid credentials'}, status=400)

# @api_view(['POST'])
# def check_login(request):
#     data = request.data
#     try:
#         user = User.objects.get(email=data['email'])
#         if check_password(data['password'], user.password):
#             serializer = UserSerializer(user)
#             return Response({'message': 'User is logged in', 'user': serializer.data}, status=200)
#         return Response({'message': 'Invalid credentials'}, status=400)
#     except User.DoesNotExist:
#         return Response({'message': 'Invalid credentials'}, status=400)
@api_view(['POST'])
def check_login(request):
    data = request.data
    try:
        # Query using the 'number' field
        user = User.objects.get(number=data['number'])
        if check_password(data['password'], user.password):
            serializer = UserSerializer(user)
            return Response({'message': 'User is logged in', 'user': serializer.data}, status=200)
        return Response({'message': 'Invalid credentials'}, status=400)
    except User.DoesNotExist:
        return Response({'message': 'Invalid credentials'}, status=400)



@api_view(['GET'])
def get_all_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=200)

@api_view(['POST', 'PUT', 'DELETE'])
def details_handler(request, pk=None):
    """
    Handle POST, PUT, DELETE for Details.
    - POST: Create a new Details record.
    - PUT: Update an existing Details record.
    - DELETE: Delete an existing Details record.
    """
    if request.method == 'POST':
        # Create a new Details record
        serializer = DetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        # Update an existing Details record
        if not pk:
            return Response({"error": "ID is required for updating details."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            details = Details.objects.get(pk=pk)
        except Details.DoesNotExist:
            return Response({"error": "Details record not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DetailsSerializer(details, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        # Delete an existing Details record
        if not pk:
            return Response({"error": "ID is required for deleting details."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            details = Details.objects.get(pk=pk)
        except Details.DoesNotExist:
            return Response({"error": "Details record not found."}, status=status.HTTP_404_NOT_FOUND)
        
        details.delete()
        return Response({"message": "Details record deleted successfully."}, status=status.HTTP_204_NO_CONTENT)