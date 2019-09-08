from django.forms import  Select, NumberInput, Textarea, TextInput, ChoiceField, CharField, DateField, DateInput, EmailField, Form, IntegerField, ModelChoiceField, ModelForm, PasswordInput, Textarea, TextInput, TimeField, TimeInput, URLField
from quizapp.models import * 
from django.forms import ModelForm 
from django import forms 

class QuestionForm(ModelForm):
    question = CharField(widget=Textarea(attrs={'class' : "form-control"}))
    answer = CharField(widget=Textarea(attrs={'class' : "form-control"}))
    category = CharField(widget=TextInput(attrs={'class' : "form-control"}))

    class Meta:
        model=Question
        fields = ['question','answer','category']