from django import forms
from django.contrib.auth.forms import UserCreationForm

from Myapp.models import Myapps

class registrationForm(UserCreationForm):
	email = forms.EmailField(max_lenght=60,help_text='Required. Add a valid email address')

	class Meta:
		model = Myapps
		fields = ("email", "username", "password1", "password2")