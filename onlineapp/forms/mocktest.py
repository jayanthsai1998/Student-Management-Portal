from onlineapp.models import MockTest1

from django import forms


class AddMarks(forms.ModelForm):
    class Meta:
        model = MockTest1
        exclude = ['id', 'student', 'total']
        widgets ={
            'problem1' : forms.NumberInput( attrs = {'class' : 'form-control' , 'placceholder' : 'Problem_1 Score'} ),
            'problem2': forms.NumberInput(attrs={'class': 'form-control', 'placceholder': 'Problem_2 Score'}),
            'problem3': forms.NumberInput(attrs={'class': 'form-control', 'placceholder': 'Problem_3 Score'}),
            'problem4': forms.NumberInput(attrs={'class': 'form-control', 'placceholder': 'Problem_4 Score'}),
        }