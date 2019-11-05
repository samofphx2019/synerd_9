from django import forms
from django.contrib.auth.forms import UserCreationForm

from Myapp.models import Myapps

class RegistrationForm(UserCreationForm):
	username = forms.CharField(label="User Name", max_lenght=200)
	password = forms.CharField(label="Password", max_lenght=200)
	firstname = forms.CharField(label="Fist Name", max_lenght=200)
	lastname = forms.CharField(label="Last Name", max_lenght=200)
	middlename = forms.CharField(label="Middle Name", max_lenght=200)
	gender = forms.CharField(label="Gender", max_lenght=100)
	address = forms.CharField(label="Address", max_lenght=200)
	city = forms.CharField(label="City", max_lenght=200)
	state = forms.CharField(label="State", max_lenght=200)
	zipcode = forms.CharField(label="Zip Code", max_lenght=200)
	email = forms.CharField(label="email", max_lenght=200)
	cellphone = forms.CharField(label="cellphone", max_lenght=100)
	country = forms.CharField(label="Country", max_lenght=200)
	dateofbirth = forms.CharField(label="Date Of Birth", max_lenght=100)
	memberogranization = forms.CharField(label="Member Organization", max_lenght=200)

	class Meta:
		model = Myapps
		fields = ("email", "password", "firstname","lastname","middlename","gender","address","city","state","zipcode","email","cellphone","country","dateofbirth","memberogranization")