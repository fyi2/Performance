from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from .models import Note, Tag


class NoteForm(forms.ModelForm):
    title = forms.CharField(
            widget=forms.TextInput(
            attrs={
                'style': 'display:table-cell; width:100%'
            }))
    text_tag = forms.CharField(
            widget=forms.TextInput(
            attrs={
                'vmodel': 'currentTag',
                'placeholder': 'Tags goes here',
                'style': 'display:table-cell; width:100%'
            }))
    class Meta:
        model = Note
        fields = ('title','text', 'text_tag')

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('user_tag',)
