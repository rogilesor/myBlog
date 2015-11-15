from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

User = get_user_model()

class LoginForm(forms.Form):
	username = forms.CharField(label="Username")
	# email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)

 
class RegisterForm(forms.Form):
	username = forms.CharField()
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)
	password2 = forms.CharField(widget=forms.PasswordInput)

	def clean_username(self):
		username = self.cleaned_data['username']
		if User.objects.filter(username=username).exists() :
			raise forms.ValidationError("username already exists")
		return username

	def clean_email(self):
		email = self.cleaned_data['email']
		if User.objects.filter(email=email).exists() :
			raise forms.ValidationError("email already exists")
		return email


	def clean(self):
		cleaned_data = super(RegisterForm,self).clean()
		password = cleaned_data.get("password")
		password2 = cleaned_data.get("password2")
		if password == password2:
			final_password = make_password(password)
			del cleaned_data['password']
			del cleaned_data['password2']
			cleaned_data['password'] = final_password
			cleaned_data['password2']= final_password

		if password != password2:
			self._errors["password"] = self.error_class(["Passwords do not match"])
			self._errors["password2"] = self.error_class(["Passwords do not match"])
			del cleaned_data['password']
			del cleaned_data['password2']
			raise forms.ValidationError("Passworrds don't match")
		return cleaned_data