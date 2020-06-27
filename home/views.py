from django.shortcuts import render,HttpResponse
from questions.models import Questions,Subject,Sub_subject
from random import random
# Create your views here.

def homeview(request):
    context={}
    dict={}
    subject=Subject.objects.all()
    for sub in subject:
        sub_subject=Sub_subject.objects.filter(subject=sub)
        dict[sub]=sub_subject
    context={'data':dict}

    return render(request,"home/home.html",context)
def aptitude(request):
    params={}
    getsubject=request.GET.get("getsubject")
    subj=Subject.objects.get(subject_name="aptitude")
    subSubject=Sub_subject.objects.filter(subject=subj)
    params={"subSubject":subSubject}
    return render(request,"home/aptitude.html",context=params)
def logical(request):
    params={}
    subj=Subject.objects.get(subject_name="logical")
    subSubject=Sub_subject.objects.filter(subject=subj)
    params={"subSubject":subSubject}
    return render(request,"home/logical.html",context=params)
def verbal(request):
    params={}
    subj=Subject.objects.get(subject_name="verbal")
    subSubject=Sub_subject.objects.filter(subject=subj)
    params={"subSubject":subSubject}
    return render(request,"home/logical.html",context=params)
def generalknowledge(request):
    params={}
    subj=Subject.objects.get(subject_name="general knowledge")
    subSubject=Sub_subject.objects.filter(subject=subj)
    params={"subSubject":subSubject}
    return render(request,"home/logical.html",context=params)
def currentaffairs(request):
    params={}
    subj=Subject.objects.get(subject_name="current affairs")
    subSubject=Sub_subject.objects.filter(subject=subj)
    params={"subSubject":subSubject}
    return render(request,"home/logical.html",context=params)
def onlinetest(request):
    questions = Questions.objects.all()
    params={'questions':questions}
    if request.method=="POST":
        length=(len(questions))
        correct_answer=0
        for i in range(1,length+1):
            answer=request.POST.get(f'option{i}')
            if answer :
                if questions[i-1].right_option==answer:
                    correct_answer+=1
                else:
                    questions[i-1].ans="incorrect"
            else:
                questions[i-1].ans="incorrect"
        params["correct_answer"]=correct_answer
        percentage=(correct_answer/10)*100
        params["percentage"]=percentage

    return render(request,'home/test.html',params)


