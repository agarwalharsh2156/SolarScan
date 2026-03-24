from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Accounts

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Accounts
        fields = ('email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Iterate through all form fields and remove the default help text
        for field in self.fields.values():
            field.help_text = ''

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Accounts
        fields = ('email', 'first_name', 'last_name')

class ProfileEditForm(forms.ModelForm):
    """Form for users to edit their profile information."""
    class Meta:
        model = Accounts
        fields = ('profile_photo', 'first_name', 'last_name', 'company_name')
        widgets = {
            'profile_photo': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name',
            }),
            'company_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Company Name',
            }),
        }