from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BookModelSerializer
from .models import BookModel


class BookListCreate(APIView):
    def get(self, request):
        books = BookModel.objects.all()
        serializer = BookModelSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        book_serializer = BookModelSerializer(data=request.data)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response(book_serializer.data, status=status.HTTP_201_CREATED)
        return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookGetUpdateDelete(APIView):
    def get(self, request, book_id):
        book = BookModel.objects.filter(id=book_id).first()
        if book:
            book_serializer = BookModelSerializer(book)
            return Response(book_serializer.data, status=status.HTTP_302_FOUND)
        return Response({'sorry': 'book not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, book_id):
        book = BookModel.objects.filter(id=book_id).first()
        if book:
            serializer = BookModelSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        return Response({'sorry': 'book not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, book_id):
        book = BookModel.objects.filter(id=book_id).first()
        if book:
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'sorry': 'book not found'}, status=status.HTTP_404_NOT_FOUND)
