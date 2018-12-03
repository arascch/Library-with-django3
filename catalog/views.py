from django.shortcuts import render
from django.views import generic
from . import models 
from django.views.generic.base import TemplateView

class index(generic.TemplateView):

    template_name ='catalog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['num_books'] = models.Book.objects.all().count()
        context ['num_instances'] = models.BookInstance.objects.all().count()
        context ['num_instances_available'] = models.BookInstance.objects.filter(status__exact='a').count()
        context ['num_author'] = models.Author.objects.all().count()
        return context


class BookListView(generic.ListView):
    model = models.Book
    template_name = 'catalog/Book_list.html'

class BookDetailView(generic.DetailView):
    model = models.Book
    template_name = 'catalog/Book_detail.html'

class AuthorlistView (generic.ListView):

    model = models.Author
    templet_name = 'catalog/author_list.html'
# def index(request) : 

#     num_books = models.Book.objects.all().count()
#     num_instance = models.BookInstance.objects.all().count()
#     num_instances_available =models.BookInstance.objects.filter(status__exact = 'a').count()
#     num_authors = models.Author.objects.count()

#     return render(
#         request , 
#         'catalog/index.html',
#         context = {'num_books' : num_books , 'num_instances' : num_instance , 'num_instaces_available' : num_instances_available , 'num_authors' : num_authors} , 
#         )



