from django.shortcuts import render
from django.http import HttpResponse

#render это специальная функция которая обрабатывает генерацию html шаблонов с переданными данными
#контроллеры обязательно принимаюе параметры request


def show_data(request):
    """Обработка GET-запроса"""
    if request.method == "GET":
        return render(request, 'app/show_data.html')


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    """Обработка POST-запрса"""
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')

        return HttpResponse(f'Спасибо, {name}, Сообщение отправлено')
    return render(request, 'catalog/contacts.html')
