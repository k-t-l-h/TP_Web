from django import forms
from .models import Question, Tag, Answer
from django.contrib.auth.models import User
from collections import OrderedDict

from django.contrib.auth import authenticate, get_user_model
from django.forms.utils import flatatt

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'text')

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('title', 'text')


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
