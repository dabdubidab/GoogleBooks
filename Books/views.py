from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView

from .models import Book


class BooksListView(ListView):
    model = Book
    template_name = 'Books/books_list.html'
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['books'] = context['books'].filter(title__icontains=search_input)
        context['search-area'] = search_input
        return context


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'
