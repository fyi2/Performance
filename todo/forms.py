from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from .models import Task, Habit


class TaskForm(forms.ModelForm):
    task = forms.CharField(
            widget=forms.TextInput(
            attrs={
                'style': 'display:table-cell; width:100%'
            }))
    task_tag = forms.CharField(
            required=False,
            widget=forms.TextInput(
            attrs={
                'vmodel': 'currentTag',
                'placeholder': 'Tags goes here',
                'style': 'display:table-cell; width:100%'
            }))
    class Meta:
        model = Task
        fields = ('task','task_tag', 'priority', 'status', 'action', 'start_date', 'due_date')

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ('habit','active_habit')
