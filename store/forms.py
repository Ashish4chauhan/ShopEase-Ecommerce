from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class CustomUserRegistrationForm(forms.ModelForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Enter username'
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class':'form-control',
            'placeholder':'Enter email'
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder':'Enter password'
        })
    )

    mobile = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Enter mobile number'
        })
    )

    address = forms.CharField(
        widget=forms.Textarea(attrs={
            'class':'form-control',
            'placeholder':'Enter address'
        })
    )

    city = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'City'
        })
    )

    state = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'State'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user