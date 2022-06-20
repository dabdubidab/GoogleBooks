import requests
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import json

from django.urls import reverse_lazy
from django.views import View
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


class ApiBooks(View):
    template_name = 'books/search_api.html'

    def get(self, request, *args, **kwargs):
        api_key = "AIzaSyDhfqtpPvrUrG1iIvtVzUx6KnSgYYB8KcI"
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            params = {'q': search_input, 'key': api_key}
            google_books = requests.get(url="https://www.googleapis.com/books/v1/volumes", params=params)
            books_json = google_books.json()
            bookshelf = books_json['items']
            books_data = []
            for elem in bookshelf:
                # for item in elem['volumeInfo'].items():
                data = []
                data.append(elem['volumeInfo']['title']),
                data.append(', '.join([i for i in elem['volumeInfo']['authors']][::])),
                data.append(int(elem['volumeInfo']['publishedDate'][:4])),
                data.append(elem['volumeInfo']['language'])
                books_data.append(data)

            return render(request, self.template_name, {'response': books_data})
        else:
            return render(request, self.template_name)

    def post(self, request):
        if self.request.method == "POST":
            title = request.POST['title']
            author = request.POST['author']
            publication_date = request.POST['publication_date']
            language = request.POST['language']
            ins = Book(title=title, author=author, publication_date=publication_date, language=language)
            ins.save()
        return render(request, self.template_name)

