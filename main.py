import django_setup

from SchoolSystem.models import Subject,Teacher,Class,Student


#форматування input
def get_input(prompt):
    return input(prompt).strip().capitalize()

def add_subject(subject:str):
    Subject(
        subject = subject
    ).save()

    return subject

def add_teacher(name:str, surname:str, email:str, age:int):
    Teacher(
        name = name,
        surname = surname,
        email = email,
        age = age
    ).save()

    return name, surname

def add_class(clas:str, specialization:str, teacher_name:str, teacher_surname:str):
    try:
        teacher = Teacher.objects.get(name=teacher_name, surname=teacher_surname)
        new_class = Class(clas=clas,
                        specialization=specialization,
                        teacher=teacher)
        new_class.save()
        return new_class
    except Teacher.DoesNotExist:
        print(f"Викладач з ім'ям {teacher_name} та прізвищем {teacher_surname} не знайдений.")

def add_student(name:str, surname:str, email:str, age:int, student_class:str):
    try:
        student_class_obj = Class.objects.get(title=student_class)
        new_student = Student(name=name,
                            surname=surname,
                            email=email,
                            age=age,
                            student_class=student_class_obj)
        new_student.save()
        return new_student
    except Class.DoesNotExist:
        print(f"Клас з назвою {student_class} не знайдено.")

    return name, surname

def add_teacher_to_subject(teacher_name: str, teacher_surname: str, subject: str):
    try:
        teacher_obj = Teacher.objects.get(name=teacher_name, surname=teacher_surname)
        subject_obj = Subject.objects.get(subject=subject)
        subject_obj.teacher.add(teacher_obj)
        print(f"Викладач {teacher_name} {teacher_surname} успішно доданий до предмету {subject}.")
    except Teacher.DoesNotExist:
        print(f"Викладач з ім'ям {teacher_name} та прізвищем {teacher_surname} не знайдений.")
    except Subject.DoesNotExist:
        print(f"Предмет з назвою {subject} не знайдений.")

def show_subjects_by_teacher(teacher_name:str, teacher_surname:str):
    try:
        teacher_obj = Teacher.objects.get(name=teacher_name, surname=teacher_surname)
        subjects_taught = teacher_obj.subject_set.all()
        if subjects_taught:
            print(f"Предмети, які викладає викладач {teacher_name} {teacher_surname}:")
            for subject in subjects_taught:
                print(subject.subject)
        else:
            print(f"Викладач {teacher_name} {teacher_surname} не викладає жодного предмета.")
    except Teacher.DoesNotExist:
        print(f"Викладач з ім'ям {teacher_name} та прізвищем {teacher_surname} не знайдений.")

def show_teachers_by_subject(subject):
    try:
        subject_obj = Subject.objects.get(subject=subject)
        teacher_taught = subject_obj.teacher.all()
        if teacher_taught:
            print(f"Викладачі які викладають {subject}:")
            for teacher in teacher_taught:
                print(teacher.name, teacher.surname)
        else:
            print(f"{subject} ніхто не викладає.")
    except Teacher.DoesNotExist:
        print(f"Такий предмет як: {subject} не знайдений.")

def show_classes_by_teacher(teacher_name:str, teacher_surname:str):
    try:
        teacher_obj = Teacher.objects.get(name=teacher_name, surname=teacher_surname)
        classes_taught = Class.objects.filter(teacher=teacher_obj)
        if classes_taught:
            print(f"Класи, які веде викладач {teacher_name} {teacher_surname}:")
            for title in classes_taught:
                print(title.title)
        else:
            print(f"Викладач {teacher_name} {teacher_surname} не веде жодного класу.")
    except Teacher.DoesNotExist:
        print(f"Викладач з ім'ям {teacher_name} та прізвищем {teacher_surname} не знайдений.")

def show_students_by_class(title):
    try:
        class_obj = Class.objects.get(title=title)
        students_taught = Student.objects.filter(student_class=class_obj)
        if students_taught:
            print(f"Студенти в класі {title}: ")
            for student in students_taught:
                print(student.name, student.surname)
        else:
            print(f"В класі {title} ніхто не навчається.")
    except Class.DoesNotExist:
        print(f"Клас {title} не знайдений.")

def show_all_subjects():
    subjects = Subject.objects.all()
    if subjects:
        print("Усі предмети:")
        for subject in subjects:
            print(subject.subject)
    else:
        print("Предмети не знайдено.")

def show_all_teachers():
    teachers = Teacher.objects.all()
    if teachers:
        print("Усі викладачі:")
        for teacher in teachers:
            print(f"{teacher.surname} {teacher.name}, електронна пошта: {teacher.email}, вік: {teacher.age}")
    else:
        print("Викладачів не знайдено.")

def show_all_classes():
    classes = Class.objects.all()
    if classes:
        print("Усі класи:")
        for class_info in classes:
            print(f"{class_info.title}, Спеціалізація класу: {class_info.specialization}")
    else:
        print("Класи не знайдено.")

def show_all_students():
    students = Student.objects.all()
    if students:
        print("Усі студенти:")
        for student in students:
            print(f"{student.surname} {student.name}, електронна пошта: {student.email}, вік: {student.age}")
    else:
        print("Студентів не знайдено.")

def choice():
    while True:
        print('''
    Виберіть дію:

    1 - Додати предмет:
    2 - Додати викладача:
    3 - Додати клас:
    4 - Додати студента:
    5 - Додати викладача до предмета:
    6 - Показати предмети за викладачем:
    7 - Показати викладача за предметом:
    8 - Показати класи за викладачем:
    9 - Показати студентів в класі:
    10 - Показати усі предмети
    11 - Показати усіх викладачів
    12 - Показати усі класи
    13 - Показати усіх студентів
    0 - Вийти:

            ''')
        command = int(get_input("Оберіть ваші дії: "))

        if command == 1:
            subject = get_input("Назва предмету: ")
            add_subject(subject)
            print(f"{subject} була успішно додано.")

        if command == 2:
            name = get_input("Ім'я: ")
            surname = get_input("Прізвище: ")
            email = get_input("Електронна пошта: ")
            age = int(get_input("Вік: "))
            add_teacher(name, surname, email, age)
            print(f"{surname} {name} був/ла успішно доданий/а.")

        if command == 3:
            clas = get_input("Клас: ")
            specialization = get_input("Спеціалізація класу: ")
            teacher_name = get_input("Ім'я класного керівника: ")
            teacher_surname = get_input("Прізвище класного керівника: ")
            add_class(clas, specialization, teacher_name, teacher_surname)
            print(f"{clas} був успішно доданий.")

        if command == 4:
            name = get_input("Ім'я: ")
            surname = get_input("Прізвище: ")
            email = get_input("Електрона пошта: ")
            age = int(get_input("Вік: "))
            student_class = get_input("Клас в якому навчається: ")
            add_student(name, surname, email, age, student_class)
            print(f"{surname} {name} був/ла успішно доданий/а.")

        if command == 5:
            teacher_name = get_input("Ім'я викладача: ")
            teacher_surname = get_input("Прізвище викладача: ")
            subject = get_input("Предмет: ")
            add_teacher_to_subject(teacher_name, teacher_surname, subject)

        if command == 6:
            teacher_name = get_input("Ім'я викладача: ")
            teacher_surname = get_input("Прізвище викладача: ")
            show_subjects_by_teacher(teacher_name, teacher_surname)

        if command == 7:
            subject = get_input("Предмет: ")
            show_teachers_by_subject(subject)

        if command == 8:
            teacher_name = get_input("Ім'я викладача: ")
            teacher_surname = get_input("Прізвище викладача: ")
            show_classes_by_teacher(teacher_name, teacher_surname)

        if command == 9:
            title = get_input("Клас: ").upper()
            show_students_by_class(title)

        if command == 10:
            show_all_subjects()

        if command == 11:
            show_all_teachers()

        if command == 12:
            show_all_classes()

        if command == 13:
            show_all_students()

        if command == 0:
            break

def main():
    choice()

if __name__ == "__main__":
    main()
