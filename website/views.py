from django.shortcuts import render

from .models import codeschool, codeacademy, contact

from .forms import ContactForm

def index(request):
    badges = codeschool.objects.all()
    languages = codeacademy.objects.all()
    return render(request, 'homepage.html', {'badges': badges, 'languages': languages})

def contact(request):
	contact = ContactForm(request.POST)
	if contact.is_valid():
		contact.save(commit=True)
		return render(request, 'thanks.html', {'contact': contact})
	else:
		contact = ContactForm()
    	return render(request, 'contact.html', {'contact': contact})

def about(request):
	return render(request, 'about.html')

