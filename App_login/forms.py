from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth.models import User
from App_login.models import Student, Teacher


class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', )


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        exclude = ('user', )


class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher
        exclude = ('user', )
