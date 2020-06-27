from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect,reverse
from questions.models import Questions,Sub_subject
from django.contrib.auth import authenticate,login,logout
from  django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User
from .models import Users
from django.contrib import messages
def EmailChecker(username,email):
    try:
        username=User.objects.get(username=username)
        email=User.objects.get(email=email)
        if username or email :
            return False
    except Exception as ex:
        return True
# Create your views here.
def register(request):
    if request.method=="POST":
        name=request.POST.get('name')
        username=request.POST.get("username")
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(password)
        mobile=request.POST.get('mobile')
        u1=EmailChecker(username,email)
        if u1:
            user = User.objects.create_user(first_name=name, email=email, password=password,username=username)
            user.save()
            stu=Users()
            stu.user=user
            stu.mobile=mobile
            stu.save()
            messages.success(request,"Registered Successfull Please Login")
            if request.GET['next']:
                return redirect(request.GET['next'])
        else:
            messages.error(request,"Username or Email already registered")
            if request.GET['next']:
                return redirect(request.GET['next'])
    else:
        messages.error(request,"Something Went Wrong")
        if request.GET['next']:
            return redirect(request.GET['next'])
@login_required
def addquestion(request,username):
    if request.user.username==username:
        subSubject=Sub_subject.objects.all()
        context={'subSubject':subSubject}
        if request.method=="POST":
            subject=request.POST.get('subject')
            question=request.POST.get('question')
            option1=request.POST.get('option1')
            option2=request.POST.get('option2')
            option3=request.POST.get('option3')
            option4=request.POST.get('option4')
            answer=request.POST.get('answer')
            description=request.POST.get('description')
            subs=Sub_subject.objects.get(sub_subject=subject)
            question=Questions(subject_type=subs,question_name=question,option1=option1,option2=option2,option3=option3,option4=option4,right_option=answer,description=description)
            question.user=request.user
            question.save()
            messages.success(request,"Question Added Successfully")
        return render(request,'accounts/addquestion.html',context)
    return redirect('homepage')
@login_required
def deletequestion(request,question_id,username):
    if request.user.username==username:
        question=Questions.objects.get(id=question_id)
        user=question.user
        if question:
            question.delete()
            messages.success(request,"Deleted Successfully")
        else:
            messages.error(request,"Question does not exists")
        return redirect('profile',user.username)
    return redirect('homepage')

def loginview(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        messages.success(request,"login success")
        permission=permissioncheck(user)
        if permission:
            return redirect('profile',user.username)
        if request.GET['next']:
            return redirect(request.GET['next'])
        # return HttpResponseRedirect(request.path_info)
    messages.error(request,"Wrong Credentials")
    if request.GET['next']:
        return redirect(request.GET['next'])



def logoutview(request):
    logout(request)
    return redirect('homepage')
@login_required
def editquestion(request,username,question_id):
    if request.user.username==username:
        user=User.objects.get(username=username)
        question=Questions.objects.get(user=user , id=question_id)
        context={'form':question}
        if request.method=="POST":
            question_name=request.POST.get('question')
            answer=request.POST.get('answer')
            option1=request.POST.get('option1')
            option2=request.POST.get('option2')
            option3=request.POST.get('option3')
            option4=request.POST.get('option4')
            description=request.POST.get('description')
            question.question_name=question_name
            question.right_option=answer
            question.option1=option1
            question.option2=option2
            question.option3=option3
            question.option4=option4
            question.description=description
            question.save()
            print("saved")
            context={'form':question}
            messages.success(request,"Updated Successfully")
        return render(request,'accounts/form.html',context=context)
    return redirect('homepage')

def registerteacher(request):
    pass

@login_required
def teacherprofile(request,username):
    if request.user.username==username:
        user=User.objects.get(username=username)
        questions=Questions.objects.filter(user=user)
        context={'questions':questions}
        return render(request,'accounts/profile.html',context=context)
    return redirect('homepage')
# decorators
def permissioncheck(user):
    for permission in user.user_permissions.all():
        if permission.name=='addquestions':
            return True
    return False