from django import forms

class ConnexionForm(forms.Form):

    username = forms.CharField(
    	widget=forms.TextInput(attrs={
    	'placeholder': 'Identifiant',
    	'name':'id', 
    	'value': '',
    	'id' : 'id'
    	}))

    password = forms.CharField(
    	widget=forms.PasswordInput(attrs={
    	'placeholder': 'Password',
    	'name':'pass', 
    	'value': '',
    	'id' : 'pass'
    	}))