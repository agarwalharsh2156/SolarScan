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