
# Create your views here.
from django.http import HttpResponse
from .models import Question
from django.http import Http404
from django.template import loader
from django.contrib.auth.models import User

def index(request):  # function view all Qqestion
    question_list = Question.objects.all();
    template = loader.get_template('question/index.html')
    context = {
        'question_list': question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id): # function views detail question
	try:
		item_question = Question.objects.get(pk=question_id)
		template = loader.get_template('question/detail.html')
		context = {
			'question': item_question,
		}
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return HttpResponse(template.render(context, request))

