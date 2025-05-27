from django.shortcuts import render

# Create your views here

def port (request):

    return render(request, 'port/home.html')


def about(request):

    return render(request, 'port/about.html')


def project(request):

    return render(request, 'port/project.html')

