from django import forms
from .models import User

class UserCreationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name','email', 'department','password', 'is_staff',)