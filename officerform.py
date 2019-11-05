from django import forms
from django.contrib.auth.forms import UserCreationForm

from Myapp.models import Myapps

class OfficerForm(UserCreationForm):
	subsriberid = forms.CharField(label="Subscriber ID", max_lenght=200)
	officecode = forms.CharField(label="Office Code", max_lenght=200)
	startdate = forms.CharField(label="Start Date", max_lenght=200)
	enddate = forms.CharField(label="End Date", max_lenght=200)
	
	class Meta:
		model = Myapps
		fields = ("Subscriber","officecode","startdate","enddate")