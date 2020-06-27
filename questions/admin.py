from django.contrib import admin
from .models import Subject,Sub_subject,Questions
# Register your models here.
admin.site.register(Questions)
admin.site.register(Subject)
admin.site.register(Sub_subject)