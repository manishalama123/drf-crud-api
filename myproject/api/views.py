from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from .serializer import PersonSerializer
from rest_framework import status, generics, mixins
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.contrib.auth import logout
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
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

#CLASS BASED VIEW
# class PersonListView(APIView):
#     def get(self, request):
#         persons = Person.objects.all()
#         serializer = PersonSerializer(persons, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = PersonSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class PersonDetailView(APIView):
#     def put(self, request, pk):
#         try:
#             person = Person.objects.get(pk=pk)
#         except Person.DoesNotExist:
#             return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = PersonSerializer(person,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data) 
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         try:
#             person = Person.objects.get(pk=pk)
#         except Person.DoesNotExist:
#             return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
#         person.delete()
#         return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

#GENERIC CLASS API VIEW

# class PersonCreateAPIView(generics.CreateAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer

# class PersonListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer

# class PersonRetrieveAPIView(generics.RetrieveAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer

# class PersonRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer


# class LogoutView(APIView):
#     def post(self, request):
#         logout(request)  # Clears session on the server
#         return Response({"message": "Logged out successfully"}, status=200)

# # MIXIN
# class PersonListCreateView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [IsAdminUser]

#     def get(self,request,*args, **kwargs):
#         return self.list(request,*args, **kwargs)
    
#     def post(self,request,*args, **kwargs):
#         return self.create(request,*args, **kwargs)

# class PersonUpdateDeleteView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
#                              mixins.DestroyModelMixin, generics.GenericAPIView):

#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer

#     def get(self,request,*args, **kwargs):
#         return self.retrieve(request,*args, **kwargs)
    
#     def put(self,request,*args, **kwargs):
#         return self.update(request,*args, **kwargs)
    
    
#     def delete(self,request,*args, **kwargs):
#         return self.destroy(request,*args, **kwargs)

#Model view Set : Simplify the CRUD
class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.id,
            'username': user.username
        })

    
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]


    def get(self, request):
        return Response({"message": "You are authenticated!", "user": request.user.username})

