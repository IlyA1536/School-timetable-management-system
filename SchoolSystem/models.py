from django.db import models

class Subject(models.Model):
    subject = models.CharField(max_length=100, unique=True)
    teacher = models.ManyToManyField("Teacher")

    def __str__(self):
        return self.subject


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.surname}"


CLASS_CHOICES = (
    ("1A", "1A"), ("1Б", "1Б"), ("1В", "1В"), ("1Г", "1Г"),
    ("2A", "2A"), ("2Б", "2Б"), ("2В", "2В"), ("2Г", "2Г"),
    ("3A", "3A"), ("3Б", "3Б"), ("3В", "3В"), ("3Г", "3Г"),
    ("4A", "4A"), ("4Б", "4Б"), ("4В", "4В"), ("4Г", "4Г"),
    ("5A", "5A"), ("5Б", "5Б"), ("5В", "5В"), ("5Г", "5Г"),
    ("6A", "6A"), ("6Б", "6Б"), ("6В", "6В"), ("6Г", "6Г"),
    ("7A", "7A"), ("7Б", "7Б"), ("7В", "7В"), ("7Г", "7Г"),
    ("8A", "8A"), ("8Б", "8Б"), ("8В", "8В"), ("8Г", "8Г"),
    ("9A", "9A"), ("9Б", "9Б"), ("9В", "9В"), ("9Г", "9Г"),
    ("10A", "10A"), ("10Б", "10Б"), ("10В", "10В"), ("10Г", "10Г"),
    ("11A", "11A"), ("11Б", "11Б"), ("11В", "11В"), ("11Г", "11Г"),
)

class Class(models.Model):
    title = models.CharField(max_length=3, choices = CLASS_CHOICES, unique=True)
    specialization = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname}"
