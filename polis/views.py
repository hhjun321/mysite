# -*- coding: utf-8 -*- 

from django.http import HttpResponse
from polis.models import Question
from django.http import Http404
from polis.method import shutdown, pingChk, openCam

from django.shortcuts import get_object_or_404, render
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polis/index.html')
    print(latest_question_list)
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polis/index.html', context)

    #return HttpResponse("hello, world. your're at the polis index.")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polis/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
	
#test중입니다.
def out(request):
    print("enter")
    ip = '172.30.1.45'
    res = pingChk(ip)
    if res==0:
        print('up')
        shutdown(ip)
    else:
        print('down')        
        
	    
    return index(request)
	
#test
def open(request):
    print("cam enter")
    openCam()
    return HttpResponseRedirect(reverse('polis:index'))