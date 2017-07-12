from django.db import models
from django.core.urlresolvers import reverse
from acct.models import User
from datetime import date



class Task(models.Model):
    user = models.ForeignKey(User)
    task_tag = models.CharField(max_length=500, default="tag", blank=True)
    task = models.CharField(max_length=250)
    slug = models.SlugField()
    start_date = models.DateField(default = date.today)
    due_date = models.DateField(default = date.today)
    created_date = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    action = models.CharField(max_length=200)

    def __unicode__(self):
        return "Task: "+self.task
    def __str__(self):
        return "Task: "+self.task


class Habit(models.Model):
    user = models.ForeignKey(User)
    habit = models.CharField(max_length=20)
    count = models.IntegerField(default=0)
    checked_date = models.DateField(default=date.today)
    start_date = models.DateField("StartDate", default=date.today)
    active_habit = models.BooleanField(default=False)

    def __unicode__(self):
        return self.habit
    def __str__(self):
        return self.habit
