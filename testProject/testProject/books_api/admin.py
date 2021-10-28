from django.contrib import admin
from .models import BookModel


@admin.register(BookModel)
class AdminBookModel(admin.ModelAdmin):
    pass

