#from django.db import models

# Create your models here.
from django.db import models


class Question(models.Model): # Создаем необходимый класс
    question_text = models.CharField(max_length=200) # Создаем 2 поля Вопрос и Дату публикации
    pub_date = models.DateTimeField('date published')
# CharField - поле из символов, DateTimeField - поле даты и времени

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # Вопрос из класса Question
    choice_text = models.CharField(max_length=200) # max_length - обязательное поле
    votes = models.IntegerField(default=0) # Кол-во голосов По умолчанию 0