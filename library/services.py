from .models import Book, Review


class BookService:

    @staticmethod
    def calculate_average_grade(book_id):
        '''Получение средней оценки'''
        reviews = Review.objects.filter(book_id=book_id)

        if not reviews.exists():
            return None

        total_score = sum(reviews.rating for reviews in reviews)
        average_score = total_score / reviews.count()

        return average_score

    @staticmethod
    def get_full_info(book_id):
        book = Book.objects.get(id=book_id)
        average_score = BookService.calculate_average_grade(book_id)
        return f'Название:{book.title} Автор:{book.author} Средняя оценка:{average_score}'

    @staticmethod
    def is_popular(book_id, threshold=4):
        # Вычисляем средний рейтинг книги
        average_rating = BookService.calculate_average_grade(book_id)
        # Если средний рейтинг не вычислен (нет отзывов), возвращаем False
        if average_rating is None:
            return False
        # Проверяем, является ли книга популярной (средний рейтинг >= порогу)
        return average_rating >= threshold

