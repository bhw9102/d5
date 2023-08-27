from django import forms


class AccountForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)