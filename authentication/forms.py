from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'New User Name'}))
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
