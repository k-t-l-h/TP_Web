from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from .models import Question, Tag, Answer
# Create your views here.

#возвращает новейшие вопросы
def hot(request):
    #здесь сортировка по датам
    context = {'question': Question.objects.all()[:3]}
    return render(request, 'ask/index.html', context)

def by_tag(request, tag):
    tmp = 'ask/tag/' + str(tag) + '.html'
    return render(request, tmp)

def by_qid(request, id):
    tmp = 'ask/question' + str(id) + '.html'
    return render(request, tmp)

def ask(request):
    return render(request, 'ask/ask.html')

def index(request):
    context = {'questions':  Question.objects.all()[:3]}
    return render(request, 'ask/index.html', context)

def login(request):
    return render(request, 'ask/login.html')

def question(request, pk):
    question = Question.objects.get(pk=pk)
    return render(request, 'ask/question.html', {'question': question})

def settings(request):
    return render(request, 'ask/settings.html')

def signup(request):
    return render(request, 'ask/signup.html')

def tag(request):
    context = {'questions':  Question.objects.all()[:6]}
    return render(request, 'ask/index.html', context)


#исправить
def paginate(objects_list, request):
    paginate_by = 5
    p = Paginator(objects_list, paginate_by)
    context = p.page()
    return context
