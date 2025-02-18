from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from .serializer import PersonSerializer
from rest_framework import status

from .models import Person
#Function based view 

# @api_view(['GET'])
# def get_user(request):
#     person = Person.objects.all()
#     serializer = PersonSerializer(person, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def post_user(request):
#     serializer = PersonSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['PUT'])
# def update_user(request, pk):
#     try:
#         person = Person.objects.get(pk=pk)
#     except Person.DoesNotExist:
#         return Response({'error': 'NOt found'}, status=status.HTTP_401_NOT_FOUND)
#     serializer = PersonSerializer(person, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['DELETE'])
# def delete_user(request, pk):
#     try:
#         person = Person.objects.get(pk=pk)
#     except Person.DoesNotExist:
#         return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

#     person.delete()
#     return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

#Class Based View
class PersonListView(APIView):
    def get(self, request):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PersonDetailView(APIView):
    def put(self, request, pk):
        try:
            person = Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PersonSerializer(person,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            person = Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        person.delete()
        return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
