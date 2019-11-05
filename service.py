from django import officeform
from django.contrib.auth.forms import UserCreationForm

from Myapp.models import Myapps

class ServiceForm(UserCreationForm):
	servicename = forms.CharField(label="Service Name", max_lenght=200)
	servicecode = forms.IntField(label="Service Code", max_lenght=200)
	decription = forms.CharField(label="Description", max_lenght=200)
	premium = forms.CharField(label="Premimum", max_lenght=200)
	allocation = forms.CharField(label="Allocation", max_lenght=200)

	class Meta:
		model = Myapps
		fields = ("servicename","servicecode","decription","premium","allocation")