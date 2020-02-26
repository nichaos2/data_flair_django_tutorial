from django import forms
from django.core import validators



def check_len_passwords(value):
    '''
    equivalent to putting the next line of code in the fields argulents:
    validators = [validators.MinLengthValidator(6)]
    '''
    if len(value)<6:
        raise forms.ValidationError("Password less tahn 6 characters")

class SignUp(forms.Form):
    first_name = forms.CharField(initial = 'First Name',)
    last_name = forms.CharField(initial = 'Last Name')
    email = forms.EmailField(help_text = 'Enter your email',required = False,)
    address = forms.CharField(required = False,)
    technology = forms.CharField(initial = 'Django', disabled=True, )
    age = forms.IntegerField(required = False,)
    password = forms.CharField(widget = forms.PasswordInput, validators = [check_len_passwords,])
    re_password = forms.CharField(help_text = 're-enter your password', 
                                  widget = forms.PasswordInput,
                                  validators = [check_len_passwords,] )

    # the function name is special, it has to be defined for each field as clean_fieldname()
    # better use validators, as above
    # def clean_password(self):
    #     password = self.cleaned_data['password']
    #     if len(password)<6:
    #         raise forms.ValidationError("password is too short")
    #     return password

    # but use it for two or more field
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data('password')
        re_password = cleaned_data('re_password')
        if password == re_password:
            raise forms.ValidationError("The password and re_password do not match")