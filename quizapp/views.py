from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect 
from quizapp.models import * 
from django import forms 
from quizapp.forms import * 
from django.urls import reverse 
import json
import requests
from random import randint
def root(request): 
    context = {}
    return render(request, 'index.html', context)

# def create_question(request): 
#     if request.method == 'GET':
#         context = {'form': QuestionForm(), 'action': '/question/create/'}
#         return render(request, 'form.html', context)
#     elif request.method == 'POST':
#         form = QuestionForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/question/create/')


def questions(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'questions.html', context)

def quiz(request):
    questions = Question.objects.all()
    question = questions[randint(0,len(questions)-1)]
    context = {'question': question}
    return render(request, 'quiz.html', context)