from django import forms
from django.forms import ModelForm,Textarea
from .models import CourseRegister,StartupRegister
from django.core.exceptions import NON_FIELD_ERRORS


class CourseRegisterForm(ModelForm):
    class Meta:
        model = CourseRegister
        fields = '__all__'
        error_messages ={
            'course':{
                'required' :  'لطفا یکی از دوره ها را انتخاب نمایید',

            },
            
            'name':{
                'required' : 'لطفا نام خود را به صورت کامل وارد نمایید',

            },
            'family':{
                'required' :  'لطفا نام خانوادگی خود را به صورت کامل وارد نمایید',

            },
            'father_name':{
                'required' : 'لطفا نام پدر خود را به صورت کامل وارد نمایید',

            },
            'meli_code':{
                'required' :  'لطفا کدملی ده رقمی خود را وارد نمایید',
                'invalid' : 'کد ملی باید فقط به صورت عددی باشد',
                'max_length' : 'کدملی باید ده رقم باشد',

            },
            'birthday':{
                'required' : 'لطفا تاریخ تولد خود را به صورت کامل وارد نمایید',
                'invalid' : 'تاریخ تولد باید بصورت روز و ماه و سال باشد',

            },
            'status':{
                'required' : 'لطفا وضعیت تحیلی خود را مشخص کنید',

            },
            'reshte':{
                'required' : 'لطفا رشته تحصیلی خود را وارد نمایید',

            },
            'uni_name':{
                'required' : 'لطفا نام محل تحصیل خود را وارد نمایید',

            },
            'phone':{
                'required' : 'لطفا شماره تماس خود را وارد نمایید',
                'invalid' : 'شماره تماس باید فقط به صورت عددی باشد',
                'max_length' : 'لطفا شماره تماس معتبر وارد نمایید',

            },
            'email':{
                'required' : 'لطفا ایمیل  خود را وارد نمایید',
                'invalid' : 'لطفا یک ایمیل معتبر وارد نمایید',

            },
            'city':{
                'required' : 'لطفا استان محل زندگی خود را وارد نمایید',
            },
        }
        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'family': forms.TextInput(attrs={'class':'form-control'}),
            'father_name': forms.TextInput(attrs={'class':'form-control'}),
            'meli_code': forms.NumberInput(attrs={'class':'form-control'}),
            'birthday': forms.TextInput(attrs={'class':'form-control fontplaceform','placeholder':'مثال : 1399/02/21'}),
            'status': forms.Select(attrs={'class':'form-control registercourses'}),
            'reshte': forms.TextInput(attrs={'class':'form-control'}),
            'uni_name': forms.TextInput(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'phone': forms.NumberInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
        }


class StartupRegisterForm(ModelForm):
    class Meta:
        model = StartupRegister
        fields = '__all__'
        error_messages ={
            'startup':{
                'required' :  'لطفا یکی از استارتاپ ها را انتخاب نمایید',

            },
            
            'name':{
                'required' : 'لطفا نام ونام خانوادگی خود را به صورت کامل وارد نمایید',

            },
            'idea_name':{
                'required' :  'لطفا عنوان ایده خود را وارد نمایید',

            },
            'idea_description':{
                'required' : 'لطفا ایده خود را شرح دهید',

            },
            'idea_status':{
                'required' :  'وضعیت ثبت ایده خود را مشخص نمایید',

            },
            'zamine':{
                'required' : 'لطفا زمینه تخصصی ایده خود را وارد نمایید',

            },
            'tarhe_jadid':{
                'required' : 'لطفا مشخص نمایید ایده در پاسخ به چه نیازی بوده؟ ',

            },
            'maziat_maayeb':{
                'required' : 'مزایا و معایب را شرح دهید',

            },
            'zaman_sakht':{
                'required' : 'لطفا زمان مورد نیاز ساخت ایده را بیان نمایید',
            },
            'manabe':{
                'required' : 'لطفا منابع توجیهی طرح را نام ببرید',
                'invalid' : 'لطفا یک ایمیل معتبر وارد نمایید',

            },
            'khalaqiat':{
                'required' : 'لطفا ابتکار و خلاقیت ایده را بیان نمایید',
            },
            'group':{
                'required' : 'لطفا نام اعضای گروه را وارد نمایید',
            },

            'status':{
                'required' : 'لطفا وضعیت تحیلی خود را مشخص کنید',

            },
            'reshte':{
                'required' : 'لطفا رشته تحصیلی خود را وارد نمایید',
            },
            'uni_name':{
                'required' : 'لطفا نام محل تحصیل خود را وارد نمایید',
            },
            'phone':{
                'required' : 'لطفا شماره تماس خود را وارد نمایید',
            },
            'email':{
                'required' : 'لطفا ایمیل خود را وارد نمایید',
                'invalid' : 'لطفا ایمیل معتبر وارد کنید'
            },
            'city':{
                'required' : 'لطفا استان محل زندگی خود را وارد نمایید',
            },
            
        }
        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'idea_name': forms.TextInput(attrs={'class':'form-control'}),
            'idea_description': forms.Textarea(attrs={'class':'form-control'}),
            'idea_status': forms.Select(attrs={'class':'form-control'}),
            'zamine': forms.TextInput(attrs={'class':'form-control '}),
            'tarhe_jadid': forms.Textarea(attrs={'class':'form-control'}),
            'maziat_maayeb': forms.Textarea(attrs={'class':'form-control'}),
            'zaman_sakht': forms.TextInput(attrs={'class':'form-control'}),
            'manabe': forms.Textarea(attrs={'class':'form-control'}),
            'khalaqiat': forms.Textarea(attrs={'class':'form-control'}),
            'group': forms.TextInput(attrs={'class':'form-control'}),
            'statux': forms.Select(attrs={'class':'form-control'}),
            'reshte': forms.TextInput(attrs={'class':'form-control'}),
            'uni_name': forms.TextInput(attrs={'class':'form-control'}),
            'phone': forms.NumberInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
        }