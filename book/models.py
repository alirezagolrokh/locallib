from django.db import models
import uuid

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100,
                            help_text='Enter a book genre(e.g. Science fiction, Romance)'
                        )


class Book(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000, 
                                help_text='Enter a brief discription of this book'
                            )
    isbn = models.CharField(max_length=13, help_text='13 characters')
    genre = models.ManyToManyField(Genre, help_text = 'select a genre of this book')
    author = models.ForeignKey('Author',
                                help_text = 'Enter author',
                                on_delete = models.SET_NULL,
                                null = True
                            )
    
    def __str__(self):
        return self.title

class Author(models.Model):
    f_name = models.CharField(max_length = 100)
    l_name = models.CharField(max_length = 100)
    birth_date = models.DateField(null = True, blank = True)
    death_date = models.DateField('Died', null = True, blank = True)

    def __str__(self):
        return '{} {}'.format(self.f_name, self.l_name)

class BookInstance(models.Model):
    id = models.UUIDField(primary_key = True,
                            default = uuid.uuid4,
                            help_text = 'uniq ID for particular book accros whol library'
                        )
    description = models.CharField(max_length=200)
    due_back = models.DateField(null = True, blank = True)
    SET_STATUS = (
                ('m', 'Maintenance'),
                ('o', 'On Loan'),
                ('r', 'Reserved'),
            )
    status = models.CharField(choices= SET_STATUS,
                                default = 'm', 
                                max_length= 20,
                                help_text = 'Book status'
                            )
    book = models.ForeignKey('Book', on_delete = models.SET_NULL, null = True)

    class Meta:
        ordering = ['due_back']


    def __str__(self):
        return '{} ({})'.format(self.id, self.book.title)