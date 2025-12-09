from django.db import models


#class ExampleStud(models.Model):
#    first_name = models.CharField(max_length=150, verbose_name='Имя')
#    last_name = models.CharField(max_length=150, verbose_name='Фамилия')

#    age = models.IntegerField(help_text='Введите возраст студента')  #Для отображения чисел
#    is_active = models.BooleanField(default=True)  #Для хранения булевых типов
#    description = models.TextField(null=True, blank=True)  #Для хранения текстовых типов,
    # null-параметр означающий может ли поле принимать пустое значение,
    # blank-параметр означающий может ли поле быть пустым в формах
#    created_at = models.DateTimeField(auto_now_add=True)  #Для хранения дат
    # auto_now_add - усатанавливает дату и время создание обьекта
    # auto_now - усатанавливает дату и время создание обьекта но изменяется при каждом обновление записи
#    image = models.ImageField(c verbase_name='Фотография')  #Для хранения изображений
    # upload_to - путь до папки куда будут сохраняться изображения для конкретной модели
#    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING, related_name='students')  #Для хранения внешнего ключа
    # PROTECT - запрещает удаление связанных записей,
    # CASCADE - при удаление группы мы удалем все связанные записи студента
    # SET_NULL - устанавливает значение в поле - NULL
    # SET_DEFAULT - устанавливает дефолтное значение
    # SET - устанавливает конкретное значение
    # DO_NOTHING - ничего не делает при удаление связанных  записей
    # related_name - имя для обратного отношения
    # on_delete - определяет поведение при удалении связанного обьекта

#    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
#    tags = models.ManyToManyField(Tag)

#    STATUS_CHOICES = [
#        ('draft', 'Draft'),
#        ('published', 'Published'),
#    ]
#    status = models.CharField(max_length=10, choises=STATUS_CHOICES, default='draft')

#    def __str__(self):
#        """Строковое отображение обьекта"""
#        return f'{self.first_name} {self.last_name}'

#    class Meta:
#        """Класс добавления в методанные"""
#        verbose_name = 'студент'
#        verbose_name_plural = 'студенты'
#        ordering = ['last_name'] #Порядок сортировки
#        db_table = 'custom_table_name'#Параметр для создания таблицы для нашей модели
class MyModel(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.descriptions} {self.updated_at} {self.created_at}'


class Student(models.Model):
    FIRST_YEAR = 'first'
    SECOND_YEAR = 'second'
    THIRD_YEAR = 'third'
    FOURTH_YEAR = 'fourth'

    YEAR_IN_SCHOOL_CHOICES = [
        (FIRST_YEAR, 'Первый курс'),
        (SECOND_YEAR, 'Второй курс'),
        (THIRD_YEAR, 'Третий курс'),
        (FOURTH_YEAR, 'Четвертый курс'),
    ]

    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    year = models.CharField(
        max_length=6,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FIRST_YEAR,
        verbose_name='Курс'
    )
    email = models.EmailField(max_length=250, verbose_name='Почта')
    enrollment_date = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'
        ordering = ['last_name']




