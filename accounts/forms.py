from django import forms
from .models import studentsignup

class studentreg(forms.ModelForm):
    sem = (('I', 'I'),
           ('II', 'II'),
           ('III', 'III'),
           ('IV', 'IV'),
           ('V', 'V'),
           ('VI', 'VI'),
           ('VII', 'VII'),
           ('VIII', 'VIII'),

           )

    dept_name = (('Dept_1', 'BTECH-CSE'),
                 ('Dept_2', 'BTECH-CIVIL'),
                 ('Dept_3', 'BTECH-MECHANICAL'),)
    roll_no = forms.CharField(widget = forms.TextInput(),required = True,max_length=25)
    name = forms.CharField(widget = forms.TextInput(),required = True,max_length=60)
    department_name = forms.ChoiceField(choices=dept_name,required = True)
    semester = forms.ChoiceField(choices=sem,required = True)

    mobile_number = forms.CharField(widget = forms.TextInput(),required = True,max_length=10)
    email_id = forms.EmailField(widget = forms.EmailInput(),required = True,max_length=20)
    password = forms.CharField(widget = forms.PasswordInput(),required = True,max_length=100)

    class Meta():
        ordering = ['roll_no']
        model = studentsignup
        fields = ['roll_no','name','department_name','semester','mobile_number','email_id','password']
