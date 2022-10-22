from dataclasses import fields
from pyexpat import model
from random import choices
from django import forms
from django.forms import ModelForm
from blog.models import Post,Category

choices = Category.objects.all().values_list('name' , 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    
    class Meta():
        model = Post
        fields = ('author','title','image','text','category')

        widgets = {
        'title': forms.TextInput(attrs={'class': 'textinputclass'}),
        'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
        }


