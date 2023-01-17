from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50 , verbose_name='Название')

    def __str__(self):
        return self.title


class Question(models.Model):
    question = models.TextField(max_length=300, verbose_name='Вопрос')
    answer = models.TextField( max_length=100, verbose_name='Ответ')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    
    def __str__(self):
        return self.question





