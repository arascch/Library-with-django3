from django.urls import path , include
from . import views
app_name = 'catalog'
urlpatterns = [
    path ('' , views.index , name = 'index'),
]