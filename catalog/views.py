from django.shortcuts import render
from . import models 


def index(request) : 

    num_book = models.Book.objects.all().count()
    num_instance = models.BookInstance.objects.all().count()
    num_instances_available =models.BookInstance.objects.filter(status_exact = 'a') . count()
    num_authors = models.Author.objects.count()

    return render(
        request , 
        'index.html',
        context = {'num_books' : num_book , 'num_instances' : num_instance , 'num_instaces_available' : num_instances_available , 'num_authors' : num_authors} , 
        )

        

