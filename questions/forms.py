from django.forms.models import ModelForm
from .models import Questions
class Teacher_Form(ModelForm):
    class Meta:
        model=Questions
        fields='__all__'
