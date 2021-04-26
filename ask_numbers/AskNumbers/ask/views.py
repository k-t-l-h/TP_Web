from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as log, logout as django_logout
from .models import Question, Tag, Answer
from .forms import *
from django.urls import reverse
# Create your views here.

#возвращает новейшие вопросы
def hot(request):
    #здесь сортировка по датам
        context = {'questions':  Question.objects.hot()}
        return render(request, 'ask/index.html', context)

def by_tag(request, tag):
    question = Question.objects.by_tag(tag)
    return render(request, {'tag': tag, 'questions': question})

def by_qid(request, id):
    tmp = 'ask/question' + str(id) + '.html'
    return render(request, tmp)

def ask(request):
    return render(request, 'ask/ask.html')

def index(request):
    context = {'questions':  Question.objects.all()[:3]}
    return render(request, 'ask/index.html', context)

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            form.clean()
            user = authenticate(username=form.cleaned_data.get('username'),
                                password=form.cleaned_data.get('password'))
            if user is not None:
                log(request, user)
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'ask/login.html', {'form': form})

def logout(request):
    django_logout(request)
    return redirect('index')

def question(request, pk):
    que = Question.objects.get(pk=pk)
    answers = Answer.objects.all().filter(question = pk)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        _title = request.POST['title']
        _text = request.POST['text']
        ans = Answer.objects.create(title = _title, text = _text, rating = 0,
         author= request.user, question = que, correct = False)
    else:
        form = AnswerForm()
    return render(request, 'ask/question.html', {'question': que, 'answers': answers, 'form': form} )

def settings(request):
    return render(request, 'ask/settings.html')

def signup(request):
    if request.method == "POST":
        #form = LoginForm(request.POST)
        _username = request.POST['username']
        _password = request.POST['password']

        us = User.objects.create_user(username=_username, password=_password)
        us.save()
        return redirect('index')
    else:
        form = SignupForm()
        return render(request, 'ask/signup.html', {'form': form})


def new_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            q = Question.objects.create(title=form.cleaned_data.get('title'),
                                        text=form.cleaned_data.get('text'), rating= 0 ,
                                        author= request.user)
            q.save()
            return redirect('question', q.pk)
        return render(request, 'ask/new_question.html',  {'form': form})
    else:
        form = QuestionForm()
        return render(request, 'ask/new_question.html',  {'form': form})

def new_answer(request):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.clean()
            a = Answer.objects.create(title=form.cleaned_data.get('title'),
                                        text=form.cleaned_data.get('text'), rating= 0,
                                        author= request.user, question = 0, correct = False)
            a.save()
            return redirect('question', q.pk)
    else:
        form = AnswerForm()
        return render(request, 'ask/new_question.html',  {'form': form})


def tag(request):
    context = {'questions':  Question.objects.all()[:6]}
    return render(request, 'ask/index.html', context)


#исправить
def paginate(objects_list, request):
    paginate_by = 5
    p = Paginator(objects_list, paginate_by)
    context = p.page()
    return context
