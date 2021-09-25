from django.shortcuts import render
from .models import Question
from django.http import HttpResponse

# Create your views here.
def index(request):
    question_list = Question.objects.all()
    context = {'question_list': question_list}
    return render(request, 'polls/index.html', context)