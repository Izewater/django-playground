from django.db import models

# Create your models here.

class Question(models.Model):
    question_test = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    #it looks like a cast question_field to string
    def __str__(self):
        return self.question_test


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    #it looks like a cast choice field to string
    def __str__(self):
        return self.choice_text
