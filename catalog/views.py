from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import cache_page

from catalog.forms import ProductForm, CategoryForm
from catalog.models import Product, Category
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin


from django.core.cache import cache

from catalog.services import CatalogService


#render это специальная функция которая обрабатывает генерацию html шаблонов с переданными данными
#контроллеры обязательно принимаюе параметры request


def show_data(request):
    """Обработка GET-запроса"""
    if request.method == "GET":
        return render(request, 'app/show_data.html')


class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        message = request.POST.get('message')

        return HttpResponse(f'Спасибо, {name}, Сообщение отправлено')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@method_decorator(cache_page(60*15), name='dispatch')
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['is_moderator'] = user.is_staff and user.groups.filter(name='Модератор продуктов').exists()
        return context


@method_decorator(cache_page(60*15), name='dispatch')
class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'

    def get_queryset(self):
        # Получаем последние 8 созданных продуктов
        products = cache.get('products_queryset')
        if products is None:
            products = Product.objects.order_by('-created_at')[:8]
            # Сохраняем данные в кеш на 15 минут (900 секунд)
            cache.set('products_queryset', products, 60*15)

        for product in products:
            print(product)

        return products


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user  # Устанавливаем владельца на текущего пользователя
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner or self.request.user.groups.filter(name='Модератор продуктов').exists()


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner or self.request.user.groups.filter(name='Модератор продуктов').exists()


class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/catalogs.html'
    context_object_name = 'categories'

    def get_queryset(self):
        """низкоуровневое кеширование"""
        queryset = cache.get('categories_queryset')

        if not queryset:
            queryset = super().get_queryset()
            cache.set('categories_queryset', queryset, 60*15)

        return queryset


@method_decorator(cache_page(60*15), name='dispatch')
class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category
    template_name = 'catalog/category_detail.html'
    context_object_name = 'category'

    slug_field = 'id'
    slug_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        # Получаем контекст от родительского класса
        context = super().get_context_data(**kwargs)
        category_id = self.object.id

        context['products'] = CatalogService.get_products_by_category(category_id)
        # Добавляем дополнительные объекты в контекст
        #context['products'] = Product.objects.filter(category=self.object)  # Дополнительный объект

        return context


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'catalog/category_form.html'
    success_url = reverse_lazy('catalog:category_list')


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'catalog/category_form.html'
    success_url = reverse_lazy('catalog:category_list')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'catalog/category_confirm_delete.html'
    success_url = reverse_lazy('catalog:category_list')


class UnpublishProductView(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)

        if not request.user.has_perm('library.can_unpublish_product'):
            return HttpResponseForbidden('У вас нет права на отмену публикации')

        product.publication_status = False
        product.save()

        return redirect('catalog:product_detail', pk=pk)


class PublishProductView(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)

        if not request.user.has_perm('library.can_publish_product'):
            return HttpResponseForbidden('У вас нет права на публикацию')

        product.publication_status = True
        product.save()

        return redirect('catalog:product_detail', pk=pk)