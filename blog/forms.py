from django import forms
from django.forms import ModelForm,Textarea
from .models import ContactUs

class ContactUsForm(ModelForm):
    class Meta:
        model =ContactUs
        fields = '__all__'
        error_messages ={
            'name':{
                'required' :  'لطفا نام خود را وارد نمایید',

            },
            'email':{
                'required' :  'لطفا ایمیل خود را وارد نمایید',

            },
            'status':{
                'required' :  'لطفا میزان اهمیت درخواست خود را مشخص نمایید',

            },
            'description':{
                'required' :  'لطفا متن خود را وارد نمایید',

            },
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-control registercourses'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),

        }

