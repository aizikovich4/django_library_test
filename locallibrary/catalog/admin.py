from django.contrib import admin
from django.db import models
from .models import Author, Genre, Book, BookInstance, Language

# Register your models here.
admin.site.register(Genre)
admin.site.register(Language)

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

# Register the Admin classes for Book using the decorator

class BooksInstanceInline(admin.TabularInline ):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre','display_language')
    inlines = [BooksInstanceInline]

# Register the Admin classes for BookInstance using the decorator

@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'due_back')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )