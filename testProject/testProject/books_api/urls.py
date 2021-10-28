from django.urls import path
from . import views


urlpatterns = [
    path('books/', views.BookListCreate.as_view(), name='list books'),
    path('books/<int:book_id>', views.BookGetUpdateDelete.as_view(), name='edit book'),

]
