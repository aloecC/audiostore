from django.urls import path
from . import views
from .views import BooksListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView, AuthorListView, \
    AuthorDetailView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView

#Пространство имен(помогает избежать ошибки при одинаковых именах маршрута)
app_name = 'library'

#В urlpatterns создаются и регестрируются маршруты
#Path это специальная функция которая позволяет регестрировать наш маршрут
urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='authors_list'),
    path('authors/<int:pk>', AuthorDetailView.as_view(), name='author_detail'),
    path('authors/new/', AuthorCreateView.as_view(), name='author_create'),
    path('authors/update/<int:pk>', AuthorUpdateView.as_view(), name='author_update'),
    path('authors/delete/<int:pk>', AuthorDeleteView.as_view(), name='author_delete'),
    #path('book_detail/<int:book_id>', views.book_detail, name='book_detail'),
    path('books/', BooksListView.as_view(), name='books_list'),
    path('books/<int:pk>', BookDetailView.as_view(), name='book_detail'),
    path('books/new/', BookCreateView.as_view(), name='books_create'),
    path('books/update/<int:pk>', BookUpdateView.as_view(), name='book_update'),
    path('books/delete/<int:pk>', BookDeleteView.as_view(), name='book_delete'),
    ]