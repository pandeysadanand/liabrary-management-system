from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.serializers import BookSerializer, UserSerializer
from books.models import Book
from user.models import User


class RegisterViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()


class BookViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookSerializer
    queryset = Book.objects.all()