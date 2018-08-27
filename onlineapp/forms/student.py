from onlineapp.models import Student

from django import forms

class AddStudent(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['id', 'dob' , 'college']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'student Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-mail address'}),
            'db_folder': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Database folder'}),
            'dropped_out': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }