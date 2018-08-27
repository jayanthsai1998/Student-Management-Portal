from django import forms

class SignUpForm(forms.Form):
    first_name = forms.CharField(
        max_length = 128,
        required = True,
        widget = forms.TextInput( attrs ={'class' : 'form-control' , 'placeholder' : 'First Name'})
    )

    last_name = forms.CharField(
        max_length=128,
        required=True,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
    )

    username = forms.CharField(
        max_length=128,
        required=True,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Name'})
    )

    password = forms.CharField(
        required=True,
        widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=128,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Name'})
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )