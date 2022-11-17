from django import forms
from .models import Topic, Target_Grade, StudentData


class StudentDataForm(forms.ModelForm):
    class Meta:
        model = StudentData
        fields = '__all__'


class TargeGradeForm(forms.ModelForm):
    class Meta:
        model = Target_Grade
        fields = '__all__'
