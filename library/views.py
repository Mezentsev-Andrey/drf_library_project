from django.utils import timezone
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from library.models import Book, BorrowedBook
from library.paginations import CustomPagination
from library.serializers import BookSerializer, BorrowedBookSerializer
from users.permissions import IsReader


class BookListAPIView(generics.ListAPIView):
    """
    Контроллер для списка книг.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    pagination_class = CustomPagination


class BorrowBookView(APIView):
    """
    Контроллер для книги взятой читателем.
    """

    permission_classes = [IsReader | IsAdminUser]

    def post(self, request, pk):
        book = generics.get_object_or_404(Book, pk=pk)
        if BorrowedBook.objects.filter(
            book=book, user=request.user, is_returned=False
        ).exists():
            return Response({"detail": "Вы уже брали эту книгу."}, status=400)
        BorrowedBook.objects.create(book=book, user=request.user)
        return Response({"detail": "Книга успешно взята для чтения."})


class ReturnBookView(APIView):
    """
    Контроллер для книги возвращенной читателем.
    """

    permission_classes = [IsReader | IsAdminUser]

    def post(self, request, pk):
        borrowed_book = generics.get_object_or_404(
            BorrowedBook, book_id=pk, user=request.user, is_returned=False
        )
        borrowed_book.is_returned = True
        borrowed_book.returned_date = timezone.now()
        borrowed_book.save()
        return Response({"detail": "Книга успешно возвращена."})


class MyBooksView(generics.ListAPIView):
    """
    Контроллер для книг на руках у читателя.
    """

    serializer_class = BorrowedBookSerializer
    permission_classes = [IsReader | IsAdminUser]

    def get_queryset(self):
        return BorrowedBook.objects.filter(user=self.request.user, is_returned=False)
