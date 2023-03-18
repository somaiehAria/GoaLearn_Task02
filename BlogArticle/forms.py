from django import forms
    
class UserRegisterForm(forms.Form):
    GENDER_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('R', 'Rather not say'),
        ('C', 'Custom')
    )
    first_name =  forms.CharField(max_length=50)
    last_name =  forms.CharField()
    age =  forms.IntegerField()
    gender =  forms.ChoiceField(choices=GENDER_CHOICES)
    mobile_number =  forms.IntegerField()
    user_name = forms.CharField()
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_Password = forms.CharField(widget=forms.PasswordInput)
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput())

