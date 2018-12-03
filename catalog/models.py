from django.db import models
from django.urls import reverse
import uuid 
class Genre (models.Model):
    #Representing book genre

    name = models.CharField(max_length =200 , help_text="Enter a book genre(e. g. science fiction , French Poetry etc.) ")
    
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author' , on_delete=models.SET_NULL , null =True)
    summary = models.TextField(max_length=1000 , help_text="enter a brief description of the book")
    isbn = models.CharField('ISBN' , max_length = 13 )
    genre = models.ManyToManyField(Genre , help_text = "select a genre for this book")

    def __str__(self) : 
        return self.title

    def get_absolute_url(self):
        return reverse('catalog:book_detail', args = [str(self.id)])

    def display_genre(self):
        """
         Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])

    display_genre.short_description = 'Genre'

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True , default = uuid.uuid4 )
    book = models.ForeignKey('Book' , on_delete=models.SET_NULL , null = True)
    imprint = models.CharField(max_length = 200)
    due_back = models.DateField(null=True , blank = True)

    LOAN_STATUS = (
        ('m' , 'Maintenance'),
        ('o' , 'On loan'),
        ('a' , 'Available'),
        ('r' , 'Reserved'),
    )

    status = models.CharField(max_length = 1 , choices = LOAN_STATUS , blank = True , default = 'm' )

    class Meta :
        ordering = ["due_back"]

    def __str__(self):
        return '%s (%s)' %(self.id , self.book.title)


class Author (models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    date_of_birth = models.DateField(null = True , blank = True)
    date_of_death = models.DateField('Died' , null = True , blank = True)

    def get_absolute_url(self):
        return reverse('catalog:author-detail' , args = [str(self.id)])

    def __str__(self):
        return '%s , %s' % (self.last_name , self.first_name)