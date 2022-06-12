from django.contrib import admin

from books.models import Book
from user.models import User

# Register your models here.
admin.site.register(User)
admin.site.register(Book)
