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
from django.http import JsonResponse
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    # PersonCreateAPIView,
    # PersonListCreateAPIView,
    # PersonRetrieveAPIView,
    # PersonRetrieveUpdateDestroyAPIView,
    # PersonListCreateView,
    # PersonUpdateDeleteView,
    # LogoutView
    # PersonViewSet,
    # CustomAuthToken,
    # ProtectedView,
    # SampleThrottle,
    # CustomThrottleView,
    AnotherView,
    BasicFiltering,
    DjangoFilterView,
    UserDetails,

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
# router = DefaultRouter()
# router.register('persons', PersonViewSet)
#Token Authentication
# urlpatterns = [
#     path('api/token/', CustomAuthToken.as_view(), name='api_token_auth'),  # Token endpoint
#     path('api/protected/', ProtectedView.as_view(), name='protected_api'),  # Protected view
#     path('', include(router.urls)),  # Register ViewSet URLs
# ]


def home(request):
    return JsonResponse({"message": "Welcome to the API! Use /api/token/ to get a token."})
urlpatterns = [
    path('', home, name='home'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Get access & refresh tokens
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Get new access token
    # path('', include(router.urls)),
    path('another/', AnotherView.as_view(), name='another-throttle'),
    # path('sample/', SampleThrottle.as_view(), name='sample-throttle'),
    # path('custom/', CustomThrottleView.as_view(), name='custom'),
    path('filter/', BasicFiltering.as_view(), name='filter'),
    # path('djfilter/', DjangoFilterView.as_view(), name='djfilter'),
    # path('searchfilter/', DjangoFilterView.as_view(), name='searchfilter')
    path('orderfilter/', DjangoFilterView.as_view(), name='orderfilter'),
    path('user/<int:pk>/', UserDetails.as_view(), name='user')
]

