from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse_lazy, reverse

from blog.models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        '''Фильтрация опубликованных статей:'''
        queryset = super().get_queryset()
        return queryset.filter(publication_sign=True)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        '''Увеличение счетчика просмотров'''
        # Получаем объект статьи
        post = super().get_object(queryset)

        post.views_count += 1  # Увеличиваем счетчик просмотров
        post.save(update_fields=['views_count'])  # Сохраняем изменения в базе данных
        return post


class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'tresh', 'image', 'publication_sign']
    success_url = reverse_lazy('blog:post_list')


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'tresh', 'image', 'publication_sign']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_list')

    def get_success_url(self):
        '''Перенаправление после редактирования'''
        return reverse('blog:post_detail', args=[self.object.pk])


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.object  # Передаем объект поста в контекст
        return context


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')