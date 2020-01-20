from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404

from django.urls import reverse

from .models import Question, Choice

# Create your views here.


def index(request):
    question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in lates_question_list])
    template = loader.get_template('somedjangoapp/index.html')
    context = {
        'latest_question_list': question_list,
    }
    # the render function/method returns a HttpResponse.
    return render(request, 'somedjangoapp/index.html', context)
    # return HttpResponse(template.render(context, request)) # classic return
    # return HttpResponse("Hello, world. My First View in python MVC Framework.")


def playground(reqeust):
    return HttpResponse('PlayGround Landing Page.')

# from documentaion


def detail(request, question_id):  # see the nameOfProject/url for url parameters
    # raising an error 404

    # SHORTHAND FOR RAISING 404

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'somedjangoapp/detail.html', {'question': question})

    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist.')
    # return render(request, 'somedjangoapp/detail.html', {'question' : question})
    # return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'somedjangoapp/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'somedjangoapp/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', args=(question.id,)))
