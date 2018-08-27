from onlineapp.models import College

from django import forms

class AddCollege(forms.ModelForm):
    class Meta:
        model = College
        exclude = ['id']
        widgets = {
            'name' : forms.TextInput( attrs ={'class' : 'form-control' , 'placeholder' : 'College Name'} ),
            'location' : forms.TextInput( attrs = {'class' : 'form-control' , 'placeholder' : 'Location'}  ),
            'acronym' : forms.TextInput(attrs = {'class' : 'form-control' , 'placeholder' : 'Acronym of College'}),
            'contact' : forms.EmailInput(attrs={'class' : 'form-control' , 'placeholder' : 'E-mail Contact'}),
        }