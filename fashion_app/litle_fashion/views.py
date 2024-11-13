from django.shortcuts import render

# Create your views here.
def home(request):
    return  render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')


def products(request):
    return render(request, 'products.html')

def about(request):
    return render(request, 'about.html')


def product_detail(request):
    return render(request, 'product-detail.html')

def sigIn(request):
    return render(request, 'signin.html')

def sigUp(request):
    return render(request, 'sign-up.html')

def faq(request):
    return render(request, 'faq.html')