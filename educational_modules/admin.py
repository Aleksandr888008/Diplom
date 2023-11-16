from django.contrib import admin

from educational_modules.models import Module


@admin.register(Module)
class HabitsAdmin(admin.ModelAdmin):
    list_display = ["title", "description"]  # отображение на дисплее
    list_filter = ["title"]  # фильтр
    search_fields = ["title"]  # поля поиска
