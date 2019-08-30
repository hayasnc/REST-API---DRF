# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from datetime import datetime    

import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=200, unique=True)
    pub_date = models.DateTimeField('date published', default=timezone.now)

    status = models.CharField(default='inactive', max_length=10)
    def __str__(self):
        return self.question_text

    def is_recent_publish(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=False)
    choice_text = models.CharField(max_length=200, null=False)
    votes = models.IntegerField(default=0)

    class Meta:
        unique_together = ['question', 'choice_text']

    def __str__(self):
        return self.choice_text
