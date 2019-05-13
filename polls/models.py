import datetime # for python

from django.db import models
from django.utils import timezone # for django.utils.timezone

# models are created below, we use class for this
# this is like building a data base for an app
# for polls, this data structure has 2 models
# Question and Choice.

# CharField, DataTimeField tells Django what type of data
# in each field

# note the __str__(self) method allows the display of object
# in the database instead of yielding only the id

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        # returns a boolean
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    # CASCADE allows the deletion of choices if the question is deleted
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    # default is an option argument
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


# 1. run "python manage.py makemigrations polls" everytime theres a change
# 2. run "python3 manage.py sqlmigrate polls 0001" to check the SQL code preparation
# 3. run "python3 manage.py check" can check without migration
# 4. finally run "python manage.py migrate" to actually migrate it


# in the python shell, first import the model class you wrote
# from polls.models import Choice, Question
# Queries can Question.objects.all(), Question.objects.filter(id=1)
# Question.objects.filter(question_text__startswith='What')
# Question.objects.get(pub_date__year=current_year)
# look up by primary key is the most common, Question.objects.get(pk=1)

# choice_set is for related models, each Choice explicity has a question field
# for reference checkout
# https://stackoverflow.com/questions/2048777/django-tutorial-what-is-choice-set
