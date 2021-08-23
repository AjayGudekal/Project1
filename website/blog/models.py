from django.db import models
from django.utils import timezone
from django import forms

class Post(models.Model):
    author=models.ForeignKey('auth.user')
    title = models.CharField(max_length=30)
    text = models.TextField()
    created_date=models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title

class EnqDB (models.Model):
    name=models.CharField(max_length=30)
    mail=models.CharField(max_length=30)
    mno=models.IntegerField()
    messege=models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Postlu(models.Model):
    author=models.CharField(max_length=30)
    title=models.CharField(max_length=30)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now())
    published_date=models.DateField(blank=True,null=True)

    def __str__(self):
        return self.author








