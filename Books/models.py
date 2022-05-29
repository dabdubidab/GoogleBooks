from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publication_date = models.DateTimeField(null=True, blank=True)
    isbn_10 = models.IntegerField(null=True, blank=True)
    isbn_13 = models.IntegerField(null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    language = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title
