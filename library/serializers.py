from django.utils import timezone
from rest_framework import serializers

from library.models import Book, BorrowedBook
from users.serializers import UserSerializer


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "author", "genre"]


class BorrowedBookSerializer(serializers.ModelSerializer):
    book_id = serializers.PrimaryKeyRelatedField(source="book", read_only=True)
    book_title = serializers.CharField(source="book.title", read_only=True)
    days_borrowed = serializers.SerializerMethodField()
    user_info = UserSerializer(source="user", read_only=True)

    class Meta:
        model = BorrowedBook
        fields = [
            "id",
            "book_id",
            "book_title",
            "user_info",
            "borrowed_date",
            "days_borrowed",
        ]

    def get_days_borrowed(self, obj):
        return (timezone.now() - obj.borrowed_date).days
