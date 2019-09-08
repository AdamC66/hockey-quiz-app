from django.db import models 
from django.forms import ModelForm 
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date 
from django import forms 
from django.contrib.auth.models import User 

class Question(models.Model):
    question= models.CharField(max_length=480)
    answer = models.CharField(max_length=480)
    category = models.CharField(max_length=63)