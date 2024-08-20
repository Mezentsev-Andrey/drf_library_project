from django.contrib import admin

from library.models import Book, BorrowedBook


class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "genre")
    list_filter = ("title", "author")
    search_fields = ("title", "author")


admin.site.register(Book, BookAdmin)


class BorrowedBookAdmin(admin.ModelAdmin):
    list_display = ("user", "book", "borrowed_date", "returned_date", "is_returned")
    list_filter = ("is_returned", "borrowed_date", "returned_date", "user")
    search_fields = ("user__username", "book__title")


admin.site.register(BorrowedBook, BorrowedBookAdmin)
