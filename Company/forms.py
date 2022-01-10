from django import forms
from django.forms import ModelForm
from .models import Agents


class UserLogin(ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserLogin, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Agents
        password = forms.CharField(widget=forms.PasswordInput)
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'Enter Password'}),
            'username': forms.TextInput(attrs={'placeholder': 'Enter Username'})
        }





