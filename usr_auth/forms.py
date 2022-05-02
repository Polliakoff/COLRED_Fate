from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Clr_Rgister_Form(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super(Clr_Rgister_Form, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
    
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={'class':'reg_psw1', 'type':'password', 'align':'center', 'placeholder':'Введите пароль'}),
    )
    password2 = forms.CharField(
        label="Подтвердите пароль",
        widget=forms.PasswordInput(attrs={'class':'reg_psw2', 'type':'password', 'align':'center', 'placeholder':'Повторите пароль'}),
    )

    class Meta:
        model = User
        fields = ["username"]
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'reg_usrnm',
                'placeholder':'Введите логин'
            })
        }
