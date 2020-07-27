from django.http import HttpResponse
from django.template import loader
from django.views.generic import View
from django.shortcuts import render, redirect
from .forms import StudentLoginForm
from .models import Student

# Create your views here.


def student_login_form(request):
    template = loader.get_template('student/loginPage.html')
    return HttpResponse(template.render())


def dashboard_view(request):
    return HttpResponse("<h1>Logged in</h1>")


class StudentLoginView(View):
    form_class = StudentLoginForm
    template_name = 'student/loginPage.html'

    # display blank form. first time opening
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # add to database. after submit
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            r_id = form.cleaned_data['registrationId']

            a = Student.objects.get(registrationId=r_id)

            if a is not None:
                return redirect('student:dashboard')
        return render(request, self.template_name, {'form': form})
