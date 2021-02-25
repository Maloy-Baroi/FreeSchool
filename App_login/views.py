from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, reverse, HttpResponseRedirect
from App_login.forms import SignupForm, TeacherForm, StudentForm


# Create your views here.
def signup_system(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)  # True or False
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('App_login:category_signup'))
    return render(request, "App_login/SignupForm.html", context={'form': form})


def login_sys(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('Home'))
    diction = {'form': form}
    return render(request, 'App_login/login.html', context=diction)


def category_signup(request):
    teacher_form = TeacherForm()
    student_form = StudentForm()
    if request.method == 'POST' and 'student_submission_btn' in request.POST:
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student = student_form.save(commit=False)
            student.user = request.user
            student.save()
            return HttpResponseRedirect(reverse('Home'))
    elif request.method == 'POST' and 'teacher_submission_btn' in request.POST:
        teacher_form = TeacherForm(request.POST)
        if student_form.is_valid():
            teacher = teacher_form.save(commit=False)
            teacher.user = request.user
            teacher.save()
            return HttpResponseRedirect(reverse('Home'))
    return render(request, "App_login/CategorySelection.html",
                  context={'teacher_form': teacher_form, 'student_form': student_form})


def logout_sys(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_login:login'))
