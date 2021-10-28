from django.db import models


class BookModel(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    description = models.TextField(max_length=100, default='')
    pages = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.pk} {self.title} {self.author}'
