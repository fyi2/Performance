from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from .models import Note, Tag


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title','text', 'text_tag')


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('user_tag',)
