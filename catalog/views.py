from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from catalog.models import Product, Category


#render это специальная функция которая обрабатывает генерацию html шаблонов с переданными данными
#контроллеры обязательно принимаюе параметры request


def show_data(request):
    """Обработка GET-запроса"""
    if request.method == "GET":
        return render(request, 'app/show_data.html')


def home(request):
    return render(request, 'catalog/home.html')


def catalogs(request):
    return render(request, 'catalog/catalogs.html')


def contacts(request):
    """Обработка POST-запрса"""
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')

        return HttpResponse(f'Спасибо, {name}, Сообщение отправлено')
    return render(request, 'catalog/contacts.html')


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
        "product": product,
    }
    return render(request, 'catalog/product_detail.html', context=context)


def product_list(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, 'catalog/home.html', context=context)


def category_list(request):
    categories = Category.objects.all()
    context = {
        "categories": categories,
    }
    return render(request, 'catalog/catalogs.html', context=context)