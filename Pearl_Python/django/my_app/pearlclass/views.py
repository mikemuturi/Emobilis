from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'pearlclass/index.html')

def about(request):
    return render(request, 'pearlclass/about.html')

def services(request):
    return render(request, 'pearlclass/services.html')

def blog(request):
    return render(request, 'pearlclass/blog.html')

def contact(request):
    return render(request, 'pearlclass/contact.html')
