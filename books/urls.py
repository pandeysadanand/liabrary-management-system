from django.urls import path

from . import views

app_name = "books"
urlpatterns = [
    path('', views.BookListView.as_view(), name="booklist"),
    path('create/', views.BooksCreateView.as_view(), name="books_create"),
    path('update/<int:pk>/', views.BooksUpdateView.as_view(), name="books_update"),
    path('delete/<int:pk>/', views.BooksDeleteView.as_view(), name="books_delete"),
]
