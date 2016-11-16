from django import forms

from django.forms import ModelForm, Textarea, TextInput

from .models import contact

class ContactForm(forms.ModelForm):
	class Meta:
		model = contact
		fields = ('name', 'email', 'phone', 'budget', 'start', 'project')
		widgets = {
		'project': Textarea(attrs={'class': 'materialize-textarea'}),
		'start': TextInput(attrs={'class': 'datepicker'})
		}