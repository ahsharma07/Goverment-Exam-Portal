from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class Subject(models.Model):
    subject_name=models.CharField(max_length=500)
    def __str__(self):
        return self.subject_name
class Sub_subject(models.Model):
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE,default=None)
    sub_subject=models.CharField(max_length=500)
    sub_description=models.TextField(default="")
    def __str__(self):
        return self.sub_subject
class Questions(models.Model):
    subject_type=models.ForeignKey(Sub_subject,on_delete=models.CASCADE,default=None)
    question_name=models.CharField(max_length=1000)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    right_option=models.CharField(max_length=100)
    description=models.TextField(default="")
    created_time=models.DateTimeField(auto_now=True)
    updated_time=models.DateTimeField(default=datetime.today())
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,default=False)
    def __str__(self):
        return self.question_name+" |User: "+self.user.username+" "