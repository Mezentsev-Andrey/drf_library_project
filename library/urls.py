from django.urls import path

from library.apps import LibraryConfig
from library.views import BookListAPIView, BorrowBookView, MyBooksView, ReturnBookView

app_name = LibraryConfig.name


urlpatterns = [
    path("books/", BookListAPIView.as_view(), name="books_list"),
    path("books/borrow/<int:pk>/", BorrowBookView.as_view(), name="borrow_book"),
    path("books/return/<int:pk>/", ReturnBookView.as_view(), name="return_book"),
    path("my_books/", MyBooksView.as_view(), name="my_books"),
]
