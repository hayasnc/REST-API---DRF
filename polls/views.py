from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from .models import Question
from django.shortcuts import render, get_object_or_404
from django.views import generic
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import Choice, Question
from polls.serializer import QuestionSerializer

@csrf_exempt
def poll(request):
    if  (request.method == 'POST'):
        # convert post data to json by jsonParser from rest_framework
        print ('sasd')
        json_parser = JSONParser()
        data = json_parser.parse(request)
        print ('&(*&(*&(*&', data)
        serializer = QuestionSerializer(data=data)
        print ('bbbb')

        if serializer.is_valid():
            print ('uu')
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            print ('jhvhv')
            return JsonResponse(serializer.errors, status=400)
    else:    
        print ('as')
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def poll_details(request, nana_id):
    print id
    try:
        instance = Question.objects.get(id=nana_id)
    except Question.DoesNotExist as e:
        return JsonResponse({"error":"Doesn't exist"}, status=404)
    if  (request.method == 'GET'):
        serializer = QuestionSerializer(instance)
        return JsonResponse(serializer.data)

    #     if serializer.is_valid():
    #         print ('uu')
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=201)
    #     else:
    #         print ('jhvhv')
    #         return JsonResponse(serializer.errors, status=400)
    # else:    
    #     print ('as')
    #     questions = Question.objects.all()
    #     serializer = QuestionSerializer(questions, many=True)
    #     return JsonResponse(serializer.data, safe=False)

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/details.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)

# def details(request, question_id):
#     try:
#         q = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Questions does't exist")
#     return render(request, 'polls/details.html', {'question': q})

# def details(request, question_id):
#     q = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/details.html', {'question': q})
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

def voting(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
