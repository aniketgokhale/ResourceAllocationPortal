from .models import Student
from django import forms


class StudentLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        db_table = 'student_info'
        model = Student
        fields = ['registrationId', 'password']
