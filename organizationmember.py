rom django import forms
from django.contrib.auth.forms import UserCreationForm

from Myapp.models import Myapps

class OrganizationMemberForm(UserCreationForm):
	orgcode = forms.IntField(label="User Name", max_lenght=200)
	subscriberid = forms.CharField(label="Password", max_lenght=200)
	membershipstartdate = forms.CharField(label="Fist Name", max_lenght=200)
	membershipenddate = forms.CharField(label="Last Name", max_lenght=200)
	country = forms.CharField(label="Middle Name", max_lenght=200)
	citizenship= forms.CharField(label="Gender", max_lenght=100)
	isdelegate = forms.CharField(label="Address", max_lenght=200)
	
	
	class Meta:
		model = Myapps
		fields = ("orgcode","subscriberid","membershipstartdate","membershipenddate","country","citizenship","isdelegate")