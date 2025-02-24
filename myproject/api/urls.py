# from django.urls import path
# from .views import PersonListView, PersonDetailView


# urlpatterns = [
#     # path('', views.get_user, name = 'get_user'), 
#     # path('create/', views.post_user, name = 'post_user'),
#     # path('<int:pk>/update/', views.update_user, name = 'update_user'),
#     # path('<int:pk>/delete/', views.delete_user, name = 'delete_user'),
#     path('', PersonListView.as_view(), name='person-list'),  
#     path('<int:pk>/', PersonDetailView.as_view(), name='person-detail'),

# ]
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    # PersonCreateAPIView,
    # PersonListCreateAPIView,
    # PersonRetrieveAPIView,
    # PersonRetrieveUpdateDestroyAPIView,
    # PersonListCreateView,
    # PersonUpdateDeleteView,
    # LogoutView
    PersonViewSet,
    CustomAuthToken,
    ProtectedView
)

# urlpatterns = [
#     # path('create/', PersonCreateAPIView.as_view(), name='person-create'),  
#     # path('', PersonListCreateAPIView.as_view(), name='person-list-create'),  
#     # path('<int:pk>/', PersonRetrieveAPIView.as_view(), name='person-retrieve'),  
#     # path('<int:pk>/update-delete/', PersonRetrieveUpdateDestroyAPIView.as_view(), name='person-update-delete'),

#     path('', PersonListCreateView.as_view(), name='person-list-create'),
#     path('<int:pk>/', PersonUpdateDeleteView.as_view(), name='person-detail'),
#     path('logout/', LogoutView.as_view(), name='logout'),

# ]
router = DefaultRouter()
router.register('persons', PersonViewSet)
urlpatterns = [
    path('api/token/', CustomAuthToken.as_view(), name='api_token_auth'),  # Token endpoint
    path('api/protected/', ProtectedView.as_view(), name='protected_api'),  # Protected view
    path('', include(router.urls)),  # Register ViewSet URLs
]

# urlpatterns = [
#     path('', include(router.urls)),
# ]