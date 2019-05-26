from django.http import HttpResponse
from polls.models.Question import Question
from django.template import loader

# Create your views here.
def index(request):
    most_recent_questions = Question.objects.all().order_by('-pub_date')[:5]
    most_recent_question_texts = [question.question_text for question in most_recent_questions]
    response = ', '.join(most_recent_question_texts)
    if (len(most_recent_question_texts) == 0):
        response = 'Currently there is no Quesition'

    context = {
        'questions': response
    }
    template = loader.get_template('polls/index.html')
    return HttpResponse(template.render(context,request))

def detail(request, question_id):
    return HttpResponse("You are looking at question %s" % question_id)

def results(request, question_id):
    return HttpResponse("You are looking at the result of the question %s" % question_id)

def vote(request, question_id):
    return HttpResponse("You are looking at the result of the question %s" % question_id)