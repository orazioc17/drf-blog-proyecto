from django.contrib import admin
from categories.models import Category


@admin.register(Category)
class QuestionAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'published']
    list_display = ('title', 'published')
    search_fields = ['title']
