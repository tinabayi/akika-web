from django.shortcuts import render,redirect
from .forms import StudentForm,FreelancerForm,EnterpriseForm,BusinessForm,AcademicForm

# Create your views here.
def welcome(request):
    return render(request, 'index.html')

def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message}) 

def student(request):
    current_user = request.user
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
           first_name = form.save(commit=False)
           last_name = form.save(commit=False)
           education_level = form.save(commit=False)
           student_email= form.save(commit=False)
            # article.editor = current_user
           first_name .save()
           last_name .save()
           education_level .save()
           student_email .save()
        return redirect('welcome')

    else:
        form = StudentForm()
    return render(request, 'student.html', {"form": form})

def freelancer(request):
    current_user = request.user
    if request.method == 'POST':
        form = FreelancerForm(request.POST, request.FILES)
        if form.is_valid():
           freelancer_names= form.save(commit=False)
           project_name = form.save(commit=False)
           freelancer_email = form.save(commit=False)
           freelancer_names .save()
           project_name .save()
           freelancer_email .save()
          
        return redirect('welcome')

    else:
        form = FreelancerForm()
    return render(request, 'freelancer.html', {"form": form})

def enterprise(request):
    current_user = request.user
    if request.method == 'POST':
        form = EnterpriseForm(request.POST, request.FILES)
        if form.is_valid():
           enterprise_founder= form.save(commit=False)
           enterprise_name = form.save(commit=False)
           enterprise_location = form.save(commit=False)
           entrprise_email= form.save(commit=False)
            # article.editor = current_user
           enterprise_founder .save()
           enterprise_name .save()
           enterprise_location .save()
           entrprise_email .save()
        return redirect('welcome')

    else:
        form =EnterpriseForm()
    return render(request, 'enterprise.html', {"form": form})

def business(request):
    current_user = request.user
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
           business_founder = form.save(commit=False)
           business_name = form.save(commit=False)
           business_location = form.save(commit=False)
           business_email= form.save(commit=False)
            # article.editor = current_user
           business_founder .save()
           business_name .save()
           business_location .save()
           business_email .save()
        return redirect('welcome')

    else:
        form = BusinessForm()
    return render(request, 'business.html', {"form": form})

def academic(request):
    current_user = request.user
    if request.method == 'POST':
        form = AcademicForm(request.POST, request.FILES)
        if form.is_valid():
           academic_name = form.save(commit=False)
           academic_location = form.save(commit=False)
           academic_email = form.save(commit=False)
          
            # article.editor = current_user

           academic_name  .save()
           academic_location .save()
           academic_email .save()
        return redirect('welcome')

    else:
        form = AcademicForm()
    return render(request, 'academic.html', {"form": form})

def student(request):
    current_user = request.user
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
           first_name = form.save(commit=False)
           last_name = form.save(commit=False)
           education_level = form.save(commit=False)
           student_email= form.save(commit=False)
            # article.editor = current_user
           first_name .save()
           last_name .save()
           education_level .save()
           student_email .save()
        return redirect('welcome')

    else:
        form = StudentForm()
    return render(request, 'student.html', {"form": form})

def student(request):
    current_user = request.user
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
           first_name = form.save(commit=False)
           last_name = form.save(commit=False)
           education_level = form.save(commit=False)
           student_email= form.save(commit=False)
            # article.editor = current_user
           first_name .save()
           last_name .save()
           education_level .save()
           student_email .save()
        return redirect('welcome')

    else:
        form = StudentForm()
    return render(request, 'student.html', {"form": form})                      