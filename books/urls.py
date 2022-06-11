from django.urls import path

from . import views

app_name = "books"
urlpatterns = [
    path('', views.BookListView.as_view(), name="booklist"),
    path('create/', views.BooksFormView.as_view(), name="books_create"),
]
