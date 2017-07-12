from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
import misaka
from django.utils.text import slugify

from todo.models import Task, Habit
from cabinet.models import Tag

from todo.forms import TaskForm, HabitForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def task_list(request, template_name='todo/task_list.html'):
    data = Task.objects.all().filter(user=request.user).order_by('-created_date')
    tasks = {}
    tasks['object_list'] = data
    data_t = Tag.objects.all().filter(user=request.user).order_by('user_tag')
    tags = {}
    tags['object_list'] = data_t
    data_h = Habit.objects.all().filter(user=request.user).order_by('habit')
    habits = {}
    habits['object_list'] = data_h

    return render(request, template_name, {'task_list': task_list,
                                          'tags':tags, 'habits':habits })
