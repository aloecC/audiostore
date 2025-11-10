from django.shortcuts import render
from django.http import HttpResponse

def example_view(request):
    return render(request, 'app/example.html')
#render это специальная функция которая обрабатывает генерацию html шаблонов с переданными данными
#контроллеры обязательно принимаюе параметры request


def show_data(request):
    """Обработка GET-запроса"""
    if request.method == "GET":
        return render(request, 'app/show_data.html')


def submit_data(request):
    """Обработка POST-запрса"""
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')

        return HttpResponse(f'Спасибо, {name}, Сообщение отправлено')
    return render(request, 'students/submit_data.html')

def show_item(request, item_id):
    """Контроллер с параметром из маршрута"""
    return render(request, 'app/item.html', {'item_id': item_id})


def about(request):
    return render(request, 'students/about.html')