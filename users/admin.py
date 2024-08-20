from django.contrib import admin

from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_reader')
    list_filter = ('is_reader',)


admin.site.register(User, UserAdmin)
