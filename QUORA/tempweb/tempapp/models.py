from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=datetime.now)  # Default value set to current datetime
    


    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField()
    pub_date = models.DateTimeField('date published')
    answer_text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answer_text
    
