from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("First blood!")

def detail(request, question_id):
    return HttpResponse("You are looking at question %s" % question_id)