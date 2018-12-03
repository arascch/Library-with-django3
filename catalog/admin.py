from django.contrib import admin
from . import models

@admin.register(models.BookInstance)

class BookinstanceAdmin(admin.ModelAdmin):
    list_filter = ('status' , 'due_back')

    fieldsets = (
        ('Information', {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

class BookInstanceInline (admin.TabularInline):
    model = models.BookInstance


@admin.register(models.Author)

class AuthorAdmin (admin.ModelAdmin):

    list_filter = ('first_name' , 'last_name')
    list_display = ('last_name' , 'first_name' , 'date_of_birth', 'date_of_death')

    field = ['first_name' , 'last_name' , ('date_of_birth' , 'date_of_birth')]

@admin.register(models.Book)

class BookAdmin (admin.ModelAdmin):
    list_display = ('title' , 'author' , 'display_genre')
    inlines = [BookInstanceInline]


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    
    list_display  = ('name',)
    