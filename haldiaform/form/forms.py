from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
	
class owner_form(forms.ModelForm):

	class Meta:

		model = owner_details
		fields = "__all__"

class room_form(forms.ModelForm):

	class Meta:

		model = Room
		fields = "__all__"
		