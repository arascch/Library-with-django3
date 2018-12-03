from django.urls import path , include
from . import views


app_name = 'catalog'

urlpatterns = [
    path ('' , views.index.as_view(), name = 'index'),
    path ('books/' , views.BookListView.as_view() , name = 'books'),
    path ('books/<int:pk>/' , views.BookDetailView.as_view() , name = 'book-detail'),
    path ('authors/' , views.AuthorlistView.as_view(), name = 'authors'),
]