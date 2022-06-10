from django.shortcuts import render
from .models import Book
# Create your views here.


def book_view(request):

    book_list = Book.objects.all()
    context = {"data": book_list}
    return render(request, "books/books.html", context)
    # if request.POST:
    #     pass
    # if request.PUT:
    #     pass
    # if request.DELETE:
    #     pass