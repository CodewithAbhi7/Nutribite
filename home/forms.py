from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['username'].error_messages = {'required': ''}
        self.fields['password1'].help_text = None
        self.fields['password1'].error_messages = {'required': ''}

