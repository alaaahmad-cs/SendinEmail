from django import forms
from .models import Email


class SEndEmail(forms.ModelForm):

    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'enter the Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email Address'}), )
    to_email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email Address'}), )
    message = forms.CharField( max_length=255, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Messages'}))
    
    class Meta:
        model = Email
        fields = ('name', 'email', 'message', 'to_email')

# class FormEmail(forms.ModelForm):
        
#     class Meta:

#         model = Email
#         fields = ('name', 'email', 'message', 'to_email')



     


