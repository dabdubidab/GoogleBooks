from django import forms
from models import Book


class SearchBookForm(forms.Form):
    key_word = forms.CharField()


