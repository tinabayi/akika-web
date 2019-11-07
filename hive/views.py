from django.shortcuts import render,redirect
from .forms import StudentForm,FreelancerForm,EnterpriseForm,BusinessForm,AcademicForm,GovernmentForm,ContactForm,CommentForm
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail
from .models import Student,Comment,StudentApplying,AcademicApplying,businessEntApplying,Government
from django.core.mail import send_mail, BadHeaderError
from .email import send_welcome_email
from .forms import NewsLetterForm
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.utils.translation import gettext as _





# Create your views here.
def welcome(request):
    return render(request, 'index.html')

def start(request):
    return render(request, 'start.html')

def search_results(request):

    if 'student' in request.GET and request.GET["student"]:
        search_term = request.GET.get("student")
        searched_student = Student.search_by_first_name(search_term)
        message = f"{search_term}"

        return render(request, 'all-hive/search.html',{"message":message,"student": searched_student})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-hive/search.html',{"message":message})


def about(request):
    return render(request, 'about.html')

def solutions(request):
    return render(request, 'solutions.html')

def solution1(request):
    return render(request, 'solution1.html')   


def contact(request):
    return render(request, 'contact.html')


def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, email, ['tblaguese1@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')
def enterpreneurship(request):
    return render(request, 'enterpreneurship.html')

def news_today(request):
    if request.method == 'POST':
        global form
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect('welcome')
        else:
            form = NewArticleForm() 
    return render(request, 'all-hive/today-news.html',{"letterForm":form})

def team(request):
    return render(request, 'team.html')

def comment(request):
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
           name = form.save(commit=False)
           comment = form.save(commit=False)
           education_level = form.save(commit=False)
           name .save()
           comment .save()
           
        return redirect('start')

    else:
        form = CommentForm()
    return render(request, 'comment.html', {"form": form})

def voir_comment(request):

           comments = Comment.objects.all()
           return render(request, 'see-comments.html',{"comments":comments})


@login_required(login_url='/accounts/login/')
def studentApply(request):
    current_user = request.user
    if request.method == 'POST':
        first_r = request.POST.get('first')
        last_r = request.POST.get('last')
        phone_r = request.POST.get('phone')
        email_r = request.POST.get('email')
        identity_r = request.POST.get('identity')
        level_r = request.POST.get('level')
        college_r = request.POST.get('institution')
        language_r = request.POST.get('language')
        

        c = studentApplying(first = first_r, last = last_r, phone = phone_r, email = email_r,identity = identity_r, level = level_r, college = college_r, language = language_r)
        c.save()
        

        return render(request, 'successfull.html')
       

        
    #Do something
    else:

         return render(request, 'studentApply.html')



@login_required(login_url='/accounts/login/')
def academicApply(request):
    current_user = request.user
    if request.method == 'POST':
        name_r = request.POST.get('name')
        email_r = request.POST.get('email')
        location_r = request.POST.get('location')
        adress_r = request.POST.get('adress')
        

        c = AcademicApplying(name = name_r, email = email_r,location = location_r, adress=adress_r)
        c.save()
        

        return render(request, 'successfull.html')
       

        
    #Do something
    else:

         return render(request, 'academicApply.html')



@login_required(login_url='/accounts/login/')    
def businessEntApply(request):
    current_user = request.user
    if request.method == 'POST':
        business_founder_r = request.POST.get('business_founder')
        business_name_r = request.POST.get('business_name')
        business_location_r = request.POST.get('business_location')
        business_email_r = request.POST.get('business_email')
        contact_number_r = request.POST.get('contact_number')
        business_type_r = request.POST.get('business_type')
        message_r = request.POST.get('message')
        other_r = request.POST.get('other')
        

        c = businessEntApplying(business_founder = business_founder_r, business_name =  business_name_r, business_location= business_location_r, business_email = business_email_r, contact_number = contact_number_r, business_type = business_type_r, message = message_r, other = other_r)
        c.save()
        

        return render(request, 'successfull1.html')
       

        
    #Do something
    else:

         return render(request, 'businessApply.html')     

@login_required(login_url='/accounts/login/')    
def governmentApply(request):
    current_user = request.user
    if request.method == 'POST':
        institution_name_r = request.POST.get(' institution_name')
        institution_location_r = request.POST.get('institution_location')
        institution_address_r = request.POST.get('institution_address')
        Contact_phone_r = request.POST.get(' Contact_phone')
        Streect_adress_r = request.POST.get('Streect_adress')
        acceptance_doc_r = request.POST.get('acceptance_doc')
        message_r = request.POST.get('message')
        other_r = request.POST.get('other')
        

        c = Government(institution_name = institution_name_r, institution_location =  institution_location_r, institution_address= institution_address_r, Contact_phone = Contact_phone_r, acceptance_doc = acceptance_doc_r, Streect_adress = Streect_adress_r, message = message_r, other = other_r)
        c.save()
        

        return render(request, 'successfull1.html')
       

        
    #Do something
    else:

         return render(request, 'governmentApply.html')     
