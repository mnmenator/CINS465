from django import forms
#from django.core.validators import validate_slug

#def must_be_caps(value):
#    if not value.isupper():
#        raise forms.ValidationError("Not all uppercase")
#    return value

class ToDoForm(forms.Form):
    #suggestion_field = forms.CharField(validators=[must_be_caps], label='Suggestion', max_length=240)'style':'width:10px'
    todo_field = forms.CharField(label='To Do:', max_length=240, widget=forms.TextInput(attrs={'class':'textInput'}))
