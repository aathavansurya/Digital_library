from django.db import models

# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=40)
    def __str__(self):
        return f'{self.course_name}'
class Book(models.Model):
    B_name=models.CharField(max_length=40)
    A_name=models.CharField(max_length=40)
    Course_id=models.ForeignKey(Course,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.B_name}'
class Student(models.Model):
    S_name=models.CharField(max_length=40)
    S_password=models.CharField(max_length=40)
    S_phone=models.BigIntegerField()
    S_semester=models.IntegerField()
    S_course_id=models.ForeignKey(Course,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.S_name}'
class Issue_book(models.Model):
    St_name=models.ForeignKey(Student,on_delete=models.CASCADE)
    Bk_name=models.ForeignKey(Book,on_delete=models.CASCADE)
    I_date=models.DateField()
    E_date=models.DateField()