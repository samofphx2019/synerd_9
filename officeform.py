from django import officeform
from django.contrib.auth.forms import UserCreationForm

from Myapp.models import Myapps

class OfficeForm(UserCreationForm):
	officname = forms.CharField(label="Office Name", max_lenght=200)
	officecode = forms.CharField(label="Office Code", max_lenght=200)
	attribution = forms.CharField(label="Attribution", max_lenght=200)
	
	class Meta:
		model = Myapps
		fields = ("officname","officecode","attribution")