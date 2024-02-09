import django_setup

from SchoolSystem.models import Subject,Teacher,Class,Student


def add_subject(subject: str):
    Subject(
        subject = subject
    ).save()

    return subject

def add_teacher(name: str, surname: str, email: str, age: int):
    Teacher(
        name = name,
        surname = surname,
        email = email,
        age = age
    ).save()

    return name, surname

def add_class(title: str, specialization: str, teacher_name: str, teacher_surname: str,):
    Class(
        title = title,
        specialization = specialization,
        teacher = Class.objects.create(teacher_name, teacher_surname)
    ).save()

    return title

def add_student(name: str, surname: str, email: str, age: int):
    Student(
        name = name,
        surname = surname,
        email = email,
        age = age
    ).save()

    return name, surname

def choice():
    while True:
            print('''
    Виберіть дію:

    1 - Додати предмет:
    2 - Додати викладача:
    3 - Додати клас:
    4 - Додати студента:
    5 - Додати викладача до предмета:
    6 - Додати клас до викладача:
    7 - Додати студента до класу:
    8 - Показати предмети за викладачем:
    9 - Показати викладача за предметом:
    10 - Показати класи за викладачем:
    11 - Показати студентів в класі:
    12 - Показати усі предмети
    13 - Показати усіх викладачів
    14 - Показати усі класи
    15 - Показати усіх студентів
    0 - Вийти:

            ''')
            command = int(input("Оберіть ваші дії: "))

            if command == 1:
                subject = input("Назва предмету: ")
                add_subject(subject)
                print(f"{subject} була успішно додано.")

            if command == 2:
                name = input("Ім'я: ")
                surname = input("Прізвище: ")
                email = input("Електронна пошта: ")
                age = int(input("Вік: "))
                add_teacher(name, surname, email, age)
                print(f"{surname} {name} був/ла успішно доданий/а.")

            if command == 3:
                pass
                # title = input("Клас: ")
                # specialization = input("Спеціалізація класу: ")
                # teacher_name = input("Класний керівник (ім'я та прізвище): ")
                # teacher_surname = input("Класний керівник (ім'я та прізвище): ")
                # try:
                #     teacher = Teacher.objects.get(name=teacher_name, surname=teacher_surname)
                #     add_class(title, specialization, teacher_name, teacher_surname)
                #     print(f"{title} був успішно доданий.")
                # except Teacher.DoesNotExist:
                #     print(f"Викладач з ім'ям {teacher_name} не знайдений.")

            if command == 4:
                pass
                # name = input("Ім'я: ")
                # surname = input("Прізвище: ")
                # email = input("Електрона пошта: ")
                # age = int(input("Вік: "))
                # add_student(name, surname, email, age)
                # print(f"{surname} {name} був/ла успішно доданий/а.")

            if command == 5:
                pass

            if command == 6:
                pass

            if command == 7:
                pass

            if command == 8:
                pass

            if command == 9:
                pass

            if command == 10:
                pass

            if command == 11:
                pass

            if command == 12:
                subjects = Subject.objects.all()
                if subjects:
                    print("Усі предмети:")
                    for subject in subjects:
                        print(subject.subject)
                else:
                    print("Предмети не знайдено.")

            if command == 13:
                teachers = Teacher.objects.all()
                if teachers:
                    print("Усі викладачі:")
                    for teacher in teachers:
                        print(f"{teacher.surname} {teacher.name}, електронна пошта: {teacher.email}, вік: {teacher.age}")
                else:
                    print("Викладачів не знайдено.")

            if command == 14:
                classes = Class.objects.all()
                if classes:
                    print("Усі класи:")
                    for class_info in classes:
                        print(f"{class_info.title}, Спеціалізація класу: {class_info.specialization}")
                else:
                    print("Класи не знайдено.")

            if command == 15:
                students = Student.objects.all()
                if students:
                    print("Усі студенти:")
                    for student in students:
                        print(f"{student.surname} {student.name}, електронна пошта: {student.email}, вік: {student.age}")
                else:
                    print("Студентів не знайдено.")

            if command == 0:
                break

def main():
    choice()

if __name__ == "__main__":
    main()
