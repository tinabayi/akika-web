from .models import Student
from .models import Freelancer
from .models import Enterprise
from .models import Business
from .models import Academic
from .models import Government
from .models import NewsLetterRecipients
from django import forms
from .models import Comment



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




class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)   

    widget=forms.TextInput(
        attrs={
            'style':'border-color:blue;'
        }
    )                            



class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['']   