from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


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


class Class(models.Model):
    title = models.CharField(max_length=3, unique=True)
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


class Schedule(models.Model):
    date = models.DateTimeField(auto_now_add=True)

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    clas = models.ForeignKey(Class, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date, self.subject, self.clas, self.teacher}"


class Grade(models.Model):
    grade = models.IntegerField(validators = [MinValueValidator(12), MinValueValidator(1)])

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.grade, self.student, self.schedule}"
