from rest_framework import serializers

from books.models import Book
from user.models import User


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name', 'author')
        read_only_fields = ('id',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password')
        read_only_fields = ('id',)
        extra_kwargs = {'password': {'write_only': True}}
