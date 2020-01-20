from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question

# Create your views here.
def index(request):
    question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in lates_question_list])
    template = loader.get_template('somedjangoapp/index.html')
    context = {
        'latest_question_list' : question_list,
    }
    return HttpResponse(template.render(context, request))
    # return HttpResponse("Hello, world. My First View in python MVC Framework.")


def playground(reqeust):
    return HttpResponse('PlayGround Landing Page.')

##from documentaion

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)