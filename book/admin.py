from django.contrib import admin

from .models import Genre
from .models import Book
from .models import Author
from .models import BookInstance

# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('f_name', 'l_name', 'birth_date')
    search_fields = ['l_name', 'f_name']    
    fields = ('birth_date',)
    list_display_links = ('f_name', 'l_name')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    search_fields = ('title',)

    def display_genre(self, obj):
        genres = [genre.name for genre in obj.genre.all()[:2]]
        return ' , '.join(genres)

    display_genre.short_description = 'Genre'


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'book_title_display', 'description', 'due_back', 'status')
    date_hierarchy  = ('due_back')
    list_filter = ('due_back', 'status')
    search_fields = ('id', 'due_back')

    def book_title_display(self,obj):
        return obj.book.title
    book_title_display.short_description = 'title'
