from djanog.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from forms import Registration

def registration_view(request):

	context = {}
	if request.POST:

		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()

			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			firstname = form.cleaned_data.get('firstname')
			middlename = form.cleaned_data.get('middlename')
			lastname = form.cleaned_data.get('lastname')
			gender = form.cleaned_data.get('gender')
			address = form.cleaned_data.get('address')
			city = form.cleaned_data.get('city')
			state = form.cleaned_data.get('state')
			zipecode = form.cleaned_data.get('zipecode')
			email = form.cleaned_data.get('email')
			cellphone = form.cleaned_data.get('cellphone')
			country = form.cleaned_data.get('country')
			dateofbrith = form.cleaned_data.get('dateofbrith')
			memeberoganization = form.cleaned_data.get('memeberoganization')

			account = authenticate(email=email, password=password1)
			login(request, account)
			return redirect('home')
		else:
		   context['registration_form'] = form
	else:
	
	    form = RegistraionForm()
	    context['registration_form'] = form
	return  render(request, 'account/registration_form.html', context)    	   	