from django.shortcuts import render
from questions.models import Sub_subject,Subject,Questions
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.
def generalknowledge(request):
    params = {}
    subj = Subject.objects.get(subject_name="general knowledge")
    subSubject = Sub_subject.objects.filter(subject=subj)
    params = {"subSubject": subSubject}
    return render(request, "home/aptitude.html", context=params)

def questions_view(request,subject):
    params={}
    question_type=Sub_subject.objects.get(sub_subject=subject)
    questions=Questions.objects.filter(subject_type=question_type)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, 15)
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    params={'questions':questions}
    return render(request,"home/questions.html",params)
