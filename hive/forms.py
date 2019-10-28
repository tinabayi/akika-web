from .models import Student
from .models import Freelancer
from .models import Enterprise
from .models import Business
from .models import Academic
from .models import Government
from django import forms



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['']

class FreelancerForm(forms.ModelForm):
    class Meta:
        model = Freelancer
        exclude = ['']

class EnterpriseForm(forms.ModelForm):
    class Meta:
        model = Enterprise
        exclude = ['']

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['']

class AcademicForm(forms.ModelForm):
    class Meta:
        model = Academic
        exclude = [''] 

class GovernmentForm(forms.ModelForm):
    class Meta:
        model = Government
        exclude = ['']                                      
        