from .models import Student, Grade


class StudentService:

    @staticmethod
    def get_full_name(student_id):
        student = Student.objects.get(id=student_id)
        return f'{student.first_name} {student.last_name}'

    @staticmethod
    def calculate_average_grade(student_id):
        '''Получение средней оценки'''
        grades = Grade.objects.filter(student_id=student_id)

        if not grades.exists():
            return None

        total_score = sum(grade.score for grade in grades)
        average_score = total_score / grades.count()

        return average_score

    @staticmethod
    def has_passed(student_id, passing_score):
        '''Метод проверки сдачи предмета'''
        average_score = StudentService.calculate_average_grade(student_id)

        if average_score is None:
            return None

        return average_score >= passing_score
