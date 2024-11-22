from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            
            Contact.objects.create(
                firstname=form.cleaned_data['firstname'],
                lastname=form.cleaned_data['lastname'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message'],
                image=form.cleaned_data['image']
            )
            return redirect('thank_you')  
    else:
        form = ContactForm()

    return render(request, 'formapp/contact.html', {'form': form})
