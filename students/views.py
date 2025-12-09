from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from students.models import Student, MyModel
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from students.forms import StudentForm


def example(request):
    return render(request, 'app/example_view.html')
#render это специальная функция которая обрабатывает генерацию html шаблонов с переданными данными
#контроллеры обязательно принимаюе параметры request


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('students:student_list')


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('students:student_list')


class MyModelCreateView(CreateView):
    model = MyModel
    fields = ['name', 'description']
    template_name = 'students/mymodel_form.html'
    success_url = reverse_lazy('students:mymodel_list')

    def form_valid(self, form):
        form.instance.create_by = self.request.user

        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        response.context_data['error_message'] = 'Please correct the errors'

        return response


class MyModelListView(ListView):
    model = MyModel
    template_name = 'students/mymodel_list.html'
    context_object_name = 'mymodels'

    def get_queryset(self):
        #queryset = super().get_queryset[].filter(is_actine=True)
        return MyModel.objects.filter(is_active=True)


class MyModelDetailView(DetailView):
    model = MyModel
    template_name = 'students/mymodel_detail.html'
    context_object_name = 'mymodel'

    def get_additional_data(self):
        return 'Это дополнительная информация'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['additional_data'] = self.get_additional_data()
        return context

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not obj.is_active:
            raise Http404('Object not found')
        return obj


class MyModelUpdateView(UpdateView):
    model = MyModel
    fields = ['name', 'description']
    template_name = 'students/mymodel_form.html'
    success_url = reverse_lazy('students:mymodel_list')


class MyModelDeleteView(DeleteView):
    model = MyModel
    template_name = 'students/mymodel_delete.html'
    success_url = reverse_lazy('students:mymodel_list')


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


def example_view(request):
    return render(request, 'students/example.html')


def index(request):
    student = Student.objects.get(id=1)
    context = {
        'student_name': f'{student.first_name} {student.last_name}',
        'student_year': student.get_year_display,
    }
    return render(request, 'students/index.html', context=context)


def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    context = {
        'student': student,
    }
    return render(request, 'students/student_detail.html', context=context)


def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'students/student_list.html', context=context)

