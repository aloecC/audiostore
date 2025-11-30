from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from catalog.models import Product, Category
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse_lazy


#render это специальная функция которая обрабатывает генерацию html шаблонов с переданными данными
#контроллеры обязательно принимаюе параметры request


def show_data(request):
    """Обработка GET-запроса"""
    if request.method == "GET":
        return render(request, 'app/show_data.html')


#def contacts(request):
#    """Обработка POST-запрса"""
#    if request.method == 'POST':
#        name = request.POST.get('name')
#        message = request.POST.get('message')
#
#        return HttpResponse(f'Спасибо, {name}, Сообщение отправлено')
#    return render(request, 'catalog/contacts.html')
class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        message = request.POST.get('message')

        return HttpResponse(f'Спасибо, {name}, Сообщение отправлено')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



#def product_detail(request, product_id):
#    product = get_object_or_404(Product, id=product_id)
#   context = {
#        "product": product,
#    }
#    return render(request, 'catalog/product_detail.html', context=context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


#def product_list(request):
#    products = Product.objects.all()
#    context = {
#        "products": products,
#    }
#    return render(request, 'catalog/home.html', context=context)


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'

#def category_list(request):
#    categories = Category.objects.all()
#    context = {
#        "categories": categories,
#    }
#    return render(request, 'catalog/catalogs.html', context=context)


class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/catalogs.html'
    context_object_name = 'categories'

#def category_detail(request, category_id):
#    category = get_object_or_404(Category, id=category_id)
#    products = Product.objects.filter(category=category)
#    context = {
#        'category': category,
#        'products': products,
#    }
#    return render(request, 'catalog/category_detail.html', context=context)


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'catalog/category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        # Получаем контекст от родительского класса
        context = super().get_context_data(**kwargs)

        # Добавляем дополнительные объекты в контекст
        context['products'] = Product.objects.filter(category=self.object)  # Дополнительный объект

        return context