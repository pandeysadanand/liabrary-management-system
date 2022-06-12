from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)
from api import views

app_name = "api"
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('register/', views.RegisterViewSet.as_view({'post': 'create'}), name='register'),
    path('books/', views.BookViewSet.as_view({'get': 'list', 'post': 'create'}), name='book_list'),
    path('books/<int:pk>/', views.BookViewSet.as_view(
        {"get": "retrieve", "put": "update", "delete": "destroy"}), name='book_detail')
]
