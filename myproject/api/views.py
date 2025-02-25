from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from .serializer import PersonSerializer
from rest_framework import status, generics, mixins
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.contrib.auth import logout
from rest_framework.viewsets import ModelViewSet
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle, ScopedRateThrottle
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.authtoken.models import Token
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
# class PersonViewSet(ModelViewSet):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer

# JWT Authentication
# class ProtectedView(APIView):
#     permission_classes = [IsAuthenticated]


#     def get(self, request):
#         return Response({"message": "You are authenticated!", "user": request.user.username})

# Throttling
class CustomThrottleView(APIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]  # Not necessary if already in settings.py

    def get(self, request):
        return Response({"message": "Throttling applied"})

class SampleThrottle(APIView):
    throttle_classes = [ScopedRateThrottle]
    # permission_classes = [IsAuthenticated]
    throttle_scope = 'sample'

    def get(self,request):
        person = Person.objects.all().order_by('id')
        paginator = CustomPagination()
        results = paginator.paginate_queryset(person, request)
        serialized_data = PersonSerializer(results, many=True)
        return paginator.get_paginated_response(serialized_data.data)
    

class AnotherView(APIView):
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'another_scope'  # This matches 'another_scope' in settings.py

    def get(self, request):
        return Response({'message': 'This is another view with a different throttle limit.'})


# class CustomPagination(PageNumberPagination):
#     page_size = 5  # Default items per page
#     page_size_query_param = 'page_size'  # Allows dynamic page size via ?page_size=10
#     max_page_size = 100  # Prevents excessive data loadingze'
# class CustomPagination(LimitOffsetPagination):
#     default_limit = 5
#     max_size = 10
class CustomPagination(CursorPagination):
    page_size = 5  # Default items per page
    ordering = 'id'