from django.http import HttpResponse
from django.template import loader


def home_page_view(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())


def choose_login_view(request):
    template = loader.get_template("chooseLogin.html")
    return HttpResponse(template.render())
