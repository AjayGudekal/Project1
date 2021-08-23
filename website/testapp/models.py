from django.db import models

class Student(models.Model) :
    sname=models.CharField(max_length=30)
    scourse=models.CharField(max_length=30)
    phno=models.IntegerField(default=0)
    email = models.EmailField(max_length=80)

    def __str__(self):
        return self.sname


class Employee(models.Model):
    empno = models.IntegerField()
    ename = models.CharField(max_length=30)
    ejob = models.CharField(max_length=30)  # <== added
    esal = models.FloatField()
    deptno = models.IntegerField(default=0)  # <==It will show 0 by default in the deptno textfield.

    def __str__(self):
        return self.ename


