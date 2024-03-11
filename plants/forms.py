from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Order

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','password1','password2')


class LoginUserForm(AuthenticationForm):
    class Meta:
        model=User
        fields=('username','password')

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name','email','address', 'city', 'country', 'credit_card_number', 'expiration_date', 'cvv']
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control '}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'country':forms.TextInput(attrs={'class':'form-control'}),
            'credit_card_number':forms.TextInput(attrs={'class':'form-control'}),
            'expiration_date':forms.TextInput(attrs={'class':'form-control'}),
            'cvv':forms.TextInput(attrs={'class':'form-control'})
        }