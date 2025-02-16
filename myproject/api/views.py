from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import PersonSerializer
from rest_framework import status

from .models import Person

@api_view(['GET'])
def get_user(request):
    person = Person.objects.all()
    serializer = PersonSerializer(person, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def post_user(request):
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

