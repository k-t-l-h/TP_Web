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

    def clean(self):
        return self.cleaned_data

    def validate(self):
        title = self.cleaned_data.get('title')
        text = self.cleaned_data.get('text')
        if title == "test" or text == "test2":
            raise forms.ValidationError("Fields are not filled")
        return self.cleaned_data


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('title', 'text')

    def clean(self):
        title = self.cleaned_data.get('title')
        text = self.cleaned_data.get('text')
        return self.cleaned_data


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Login is invalid. User is not found")
        return self.cleaned_data

class SignupForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control col-sm-6'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control col-sm-6'}))

    class Meta:
        model = User
        fields = ('username', 'password', 'confirm_password')


    def clean(self):
        confirm_password = self.cleaned_data.get('confirm_password')
        password = self.cleaned_data.get('password')

        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match')
