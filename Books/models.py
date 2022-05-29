from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publication_date = models.DateTimeField(null=True, blank=True)
    isbn_10 = models.IntegerField(blank=True)
    isbn_13 = models.IntegerField(blank=True)
    pages = models.IntegerField(blank=True)
    link = models.URLField(blank=True)
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.title
