from django.shortcuts import render

from library.forms import BookForm, AuthorForm
from library.models import Book, Author
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy


class AuthorListView(ListView):
    model = Author
    template_name = 'author/authors_list.html'
    context_object_name = 'authors'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author/author_detail.html'
    context_object_name = 'author'


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author/author_form.html'
    success_url = reverse_lazy('library:books_list')


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author/author_form.html'
    success_url = reverse_lazy('library:books_list')


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'author/author_confirm_delete.html'
    success_url = reverse_lazy('library:authors_list')


class BooksListView(ListView):
    model = Book
    template_name = 'book/books_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        # Получаем только книги опубликованные после 2000
        queryset = super().get_queryset()
        return queryset


class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    context_object_name = 'book'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_books_count'] = Book.objects.filter(author=self.object.author).count()
        return context


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book/book_form.html'
    success_url = reverse_lazy('library:books_list')


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book/book_form.html'
    success_url = reverse_lazy('library:books_list')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book/book_confirm_delete.html'
    success_url = reverse_lazy('library:books_list')




#def book_detail(request, book_id):
 #   book = get_object_or_404(Book, id=book_id)
 #   context = {
 #       "book": book
  #  }

 #   return render(request, 'book/book_detail.html', context=context)


#def book_list(request):
 #   books = Book.objects.all()
  #  context = {
   #     "books": books
   # }
   # return render(request, "book/book_list.html", context=context)