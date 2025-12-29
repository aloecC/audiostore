from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.views import View

from library.forms import BookForm, AuthorForm
from library.models import Book, Author
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from django.core.cache import cache

from library.services import BookService


class AuthorListView(ListView):
    model = Author
    template_name = 'author/authors_list.html'
    context_object_name = 'authors'

    def get_queryset(self):
        """низкоуровневое кеширование"""
        queryset = cache.get('authors_queryset')

        if not queryset: # если в кеше нет значения то мы ищем его в БД
            queryset = super().get_queryset()
            cache.set('authors_queryset', queryset, 60*15)
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


@method_decorator(cache_page(60*15), name='dispatch')
class BooksListView(ListView):
    model = Book
    template_name = 'book/books_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        # Получаем только книги опубликованные после 2000
        queryset = super().get_queryset()
        return queryset


@method_decorator(cache_page(60*15), name='dispatch')
class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_id = self.object.id

        context['full_info'] = BookService.get_full_info(book_id)

        context['average_grade'] = BookService.calculate_average_grade(book_id)


        context['author_books_count'] = Book.objects.filter(author=self.object.author).count()

        return context



class BookCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book/book_form.html'
    permission_required = 'library.add_book'
    success_url = reverse_lazy('library:books_list')


class BookUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book/book_form.html'
    permission_required = 'library.change_book'
    success_url = reverse_lazy('library:books_list')


class BookDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = 'book/book_confirm_delete.html'
    permission_required = 'library.delete_book'
    success_url = reverse_lazy('library:books_list')


class ReviewBookView(LoginRequiredMixin, View):
    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)

        if not request.user.has_perm('library.can_review_book'):
            return HttpResponseForbidden('У вас нет права на рецензию')

        book.review = request.POST.get('review')
        book.save()

        return redirect('library:book_detail', pk=book_id)


class RecommendBookView(LoginRequiredMixin, View):
    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)

        if not request.user.has_perm('library.can_recommend_book'):
            return HttpResponseForbidden('У вас нет права на рекомендацию')

        book.recommend = True
        book.save()

        return redirect('library:book_detail', pk=book_id)