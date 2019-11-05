from django import forms
from django.contrib.auth.forms import UserCreationForm

from Myapp.models import Myapps

class OrganizationForm(UserCreationForm):
	orgname = forms.CharField(label="User Name", max_lenght=200)
	orgcode = forms.CharField(label="Password", max_lenght=200)
	description = forms.CharField(label="Fist Name", max_lenght=200)
	datejoine = forms.CharField(label="Last Name", max_lenght=200)
	address1 = forms.CharField(label="Middle Name", max_lenght=200)
	address2= forms.CharField(label="Gender", max_lenght=100)
	city = forms.CharField(label="Address", max_lenght=200)
	state = forms.CharField(label="City", max_lenght=200)
	zipcode = forms.CharField(label="State", max_lenght=200)
	phonenumber = forms.CharField(label="Zip Code", max_lenght=200)
	
	class Meta:
		model = Myapps
		fields = ("orgname","orgcode","description","datejoine","address1","address2","city","state","zipcode","phonenumber")