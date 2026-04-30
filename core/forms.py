from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control custom-input', 'placeholder': 'NAME'}),
            'email': forms.EmailInput(attrs={'class': 'form-control custom-input', 'placeholder': 'EMAIL'}),
            'subject': forms.TextInput(attrs={'class': 'form-control custom-input', 'placeholder': 'SUBJECT'}),
            'message': forms.Textarea(attrs={'class': 'form-control custom-input', 'placeholder': 'ABOUT THE MESSAGE', 'rows': 4}),
        }