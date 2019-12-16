from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from django import forms

class QManager(models.Manager):
    def hot(self, page_number, limit):
        return paginator.paginate(
            self.order_by('-rating'), limit, page_number)

    def questions_by_tag(self, tag_name, page_number, limit):
        t = Tag.objects.get(name=tag_name)
        return paginator.paginate(self.filter(tag=t), limit, page_number)



class Question(models.Model):
    objects = QManager()
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(to='Tag', related_name='questions')
    answers = models.IntegerField(default=0)

class Tag(models.Model):
    text = models.SlugField(unique=True)

    def __get__(self):
        return self.text

class AManager(models.Manager):
    def hot(self, page_number, limit):
        return paginator.paginate(
            self.order_by('-rating'), limit, page_number)


#вынести в менеджер
class Answer(models.Model):
    objects = AManager()

    title = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey('Question', null=True, on_delete=models.CASCADE)
    correct = models.BooleanField(default=False)

    @classmethod
    def __answer__(self, _question, _author, _text, _title):
        new_answer = self.objects.create(title = _title, text = _text, author = _author,
        question = _question, rating = 0, correct = False)
        return new_answer


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __init__(self, _user):
        new_user = self.objects.create(user = _user)
        return new_answer

#uniqe together
class QLike(models.Model):
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    value = models.IntegerField(default=0)
    class Meta:
        unique_together = (("question", "user"),)

class ALike(models.Model):
    answer = models.ForeignKey(to=Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    value = models.IntegerField(default=0)

    class Meta:
        unique_together = (("answer", "user"),)
