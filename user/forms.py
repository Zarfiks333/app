from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from user.models import User

class UserLoginForm(AuthenticationForm):

    username =  forms.CharField()
    password = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 
                  'password',
                  ]


class UserRegistrationForm(UserCreationForm):

    username =  forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = [
            'username', 
            'email',
            'password1',
            'password2',
            ]

class ProfileForm(UserChangeForm):
    
    class Meta:
        model = User
        fields = [
            "image",
            'username', 
            ]
        
        widgets = {

            'image': forms.FileInput(attrs= {'class':'avatar_form_label', 'required': False,}),
            'username': forms.TextInput(attrs= {'class':'nikname_form_input'}),

        }
        
