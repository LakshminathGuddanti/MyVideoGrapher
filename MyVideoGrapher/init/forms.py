from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.forms import widgets
from init.models import CamModels, OrderModel, User

class VideoGrapherRegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control my-2',
        'placeholder':'Enter Password',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control my-2',
        'placeholder':'Enter Confirm Password',
    }))
    class Meta:
        model = User    
        fields = ['first_name','last_name','username','email','password1','password2']
        widgets = {
            'first_name':forms.TextInput(attrs={
                'class':'form-control my-2',
                'placeholder':'Enter First Name',
            }),
            'last_name':forms.TextInput(attrs={
                'class':'form-control my-2',
                'placeholder':'Enter Last Name',
            }),
            'username':forms.TextInput(attrs={
                'class':'form-control my-2',
                'placeholder':'Enter UserName',
            }),
            'email':forms.TextInput(attrs={
                'class':'form-control my-2',
                'placeholder':'Enter Your Email Address',
            }),
        }


class VideoGrapherProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','studio_name','vaddress','experience','Description','profileImag']
        widgets = {
            'first_name':forms.TextInput(attrs={
                'class':'form-control my-2',
                'placeholder':'Enter First Name',
            }),
            'last_name':forms.TextInput(attrs={
                'class':'form-control my-2',
                'placeholder':'Enter Last Name',
            }),
            'username':forms.TextInput(attrs={
                'class':'form-control my-2',
                'placeholder':'Enter UserName',
            }),
            'email':forms.TextInput(attrs={
                'class':'form-control my-2',
                'placeholder':'Enter Your Email Address',
            }),
            'studio_name':forms.TextInput(attrs={
                'class':'form-control my-2',
                'placeholder':'Enter name of the Studio',
            }),
            'vaddress':forms.Textarea(attrs={
                'class':'form-control my-2',
                'placeholder':'Enter The Address in the format of \nlocalAddress,\ncity,\ndistict,\nstate,\ncountry',
                'rows':8,
            }),
            'experience':forms.NumberInput(attrs={
                'class':'form-control my-2',
                'placeholder':'Enter Your experience ',
            }),
            'Description':forms.Textarea(attrs={
                'class':'form-control my-2',
                'placeholder':'Place a brief description upon your studio',
                'rows':3,
            }),
        }

class CamForm(forms.ModelForm):
    class Meta:
        model = CamModels
        fields = ['camName','prizePerHour','description','camPic']
        widgets = {
            'camName':forms.TextInput(attrs={
                'class':'form-control my-2',
                'placeholder':'Enter name of Camara',   
            }),
            'prizePerHour':forms.TextInput(attrs={
                'class':'form-control my-2',
                'placeholder':'Enter Charge per Day',
            }),
            'description':forms.Textarea(attrs={
                'class':'form-control my-2',
                'placeholder':'Describe Briefly about your camara',
                'rows':2,
            }),
        }


class UserRegistForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control my-2',
        'placeholder':'Enter Password',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control my-2',
        'placeholder':'Enter Confirm Password',
    }))
    class Meta:
        model = User    
        fields = ['first_name','last_name','username','email','password1','password2']
        widgets = {
            'first_name':forms.TextInput(attrs={
                'class':'form-control my-2',
                'placeholder':'Enter First Name',
            }),
            'last_name':forms.TextInput(attrs={
                'class':'form-control my-2',
                'placeholder':'Enter Last Name',
            }),
            'username':forms.TextInput(attrs={
                'class':'form-control my-2',
                'placeholder':'Enter UserName',
            }),
            'email':forms.TextInput(attrs={
                'class':'form-control my-2',
                'placeholder':'Enter Your Email Address',
            }),
        }


class CustomerProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        widgets = {
            'first_name':forms.TextInput(attrs={
                'class':'form-control my-2',
                'placeholder':'Enter First Name',
            }),
            'last_name':forms.TextInput(attrs={
                'class':'form-control my-2',
                'placeholder':'Enter Last Name',
            }),
            'username':forms.TextInput(attrs={
                'class':'form-control my-2',
                'placeholder':'Enter UserName',
            }),
            'email':forms.TextInput(attrs={
                'class':'form-control my-2',
                'placeholder':'Enter Your Email Address',
            }),
        }

class PasswordChange(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control my-2',
        'placeholder':'Enter Old Password',
    }))
    
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control my-2',
        'placeholder':'Enter New Password',
    }))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control my-2',
        'placeholder':'Enter new Confirm Password',
    }))
    class Meta:
        model = User
        fields = ['old_password','new_password1','new_password2']
        widgets = {
            'old_password':forms.PasswordInput(attrs={
                'class':'form-control my-2',
                'placeholder':'Enter The password',
            }),
            'new_password1':forms.PasswordInput(attrs={
                'class':'form-control my-2',
                'placeholder':'Enter The password',
            }),
            'new_password2':forms.PasswordInput(attrs={
                'class':'form-control my-2',
                'placeholder':'Enter The password',
            }),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        fields = ['nameOfEvent','email','fromDate','toDate','ceremonyTime','addressOfCeremony']
        widgets = {
            "nameOfEvent":forms.TextInput(attrs={
                'class':'form-control my-2',
                'placeholder':'Name of the Event',
            }),
            'fromDate':forms.DateInput(attrs={
                'class':'form-control my-2',
                'type':'date',
            }),
            'toDate':forms.DateTimeInput(attrs={
                'class':'form-control my-2',
                'type':'date',
            }),
            'ceremonyTime':forms.DateTimeInput(attrs={
                'class':'form-control my-2',
                'type':'datetime-local',
            }),
            'addressOfCeremony':forms.Textarea(attrs={
                'class':'form-control my-2',
                'placeholder':'Location of Event',
                'rows':3,
            }),
            'email':forms.TextInput(attrs={
                'class':'form-control my-2',
                'placeholder':'Enter Your Email Address',
                
            }),
        }

class viewCustOrderForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        fields = ['nameOfEvent','email','fromDate','toDate','ceremonyTime','addressOfCeremony','isAccepted']
        widgets = {
            "nameOfEvent":forms.TextInput(attrs={
                'class':'form-control my-2',
                'placeholder':'Name of the Event',
                'readonly':True
            }),
            'fromDate':forms.DateInput(attrs={
                'class':'form-control my-2',
                'type':'date',
                'readonly':True
            }),
            'toDate':forms.DateTimeInput(attrs={
                'class':'form-control my-2',
                'type':'date',
                'readonly':True
            }),
            'ceremonyTime':forms.DateTimeInput(attrs={
                'class':'form-control my-2',
                'type':'datetime-local',
                'readonly':True
            }),
            'addressOfCeremony':forms.Textarea(attrs={
                'class':'form-control my-2',
                'placeholder':'Location of Event',
                'rows':3,
                'readonly':True
            }),
            'isAccepted':forms.Select(attrs={
                'class' : 'form-control my-2',
            }),
            'email':forms.TextInput(attrs={
                'class':'form-control my-2',
                'placeholder':'Enter Your Email Address',
                'readonly':True,
            }),            
        }
