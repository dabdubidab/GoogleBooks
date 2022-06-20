from django.urls import path
from .views import BooksListView, BookDetailView, ApiBooks

urlpatterns = [
    path('books-list/', BooksListView.as_view(), name='books-list'),
    path('book-detail/<pk>/', BookDetailView.as_view(), name='book-detail'),
    path('search-api/', ApiBooks.as_view(), name='search-api')
]
