from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from django.template import loader
from .models import Question, Choice
from django.views import generic
from django.contrib import messages

def index(request):
    return HttpResponse("Hola, esta huevá ha funcionado y la concha de sumadre.")


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    model = Question
    template_name = 'polls/vote.html'

    ... # same as above, no changes needed.