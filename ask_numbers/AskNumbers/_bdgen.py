import sys
import os
import django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'AskNumbers.settings'
django.setup()

from django.contrib.auth.models import User
from ask.models import Question, Tag, Profile
from django.contrib.auth.models import User
from faker import Faker
from random import randint

fake = Faker()


for i in range(10 000):
    us = User.objects.create_user(username='user_#{}'.format(i), password='pass')
    us.save()

tags_num = 0
for i in range(10 000):
    tag = Tag.objects.create(text=fake.word())
    tag.save()
    tags_num += 1

taglist = list(Tag.objects.all())

for i in range(100 000):
    q = Question.objects.create(title=fake.sentence(),
                                text=' '.join(fake.sentences()), rating=0,
                                author=list(User.objects.all())
                                [randint(0, len(User.objects.all())-1)])
    q.save()
