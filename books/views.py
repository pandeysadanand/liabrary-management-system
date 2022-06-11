from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import BooksForm
from .models import Book


# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'books/books.html'


class BooksCreateView(CreateView):
    template_name = 'books/create.html'
    form_class = BooksForm
    success_url = '/books/'


class BooksUpdateView(UpdateView):
    template_name = 'books/create.html'
    form_class = BooksForm
    success_url = '/books/'
    queryset = Book.objects.all()


class BooksDeleteView(DeleteView):
    template_name = 'books/pre_delete.html'
    model = Book
    success_url = '/books/'
