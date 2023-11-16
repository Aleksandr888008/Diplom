from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["email", "first_name", "last_name"]  # отображение на дисплее
    list_filter = ["email", "first_name"]  # фильтр
    search_fields = ["email", "first_name", "last_name"]  # поля поиска
