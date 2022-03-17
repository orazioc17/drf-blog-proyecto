from django.contrib import admin
from categories.models import Category


@admin.register(Category)
class QuestionAdmin(admin.ModelAdmin):
    fields = ['name', 'description']
    list_display = ('name', 'description')
    search_fields = ['name']
