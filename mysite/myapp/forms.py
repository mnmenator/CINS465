from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from django.core.validators import validate_slug

#def must_be_caps(value):
#    if not value.isupper():
#        raise forms.ValidationError("Not all uppercase")
#    return value

class ChirpForm(forms.Form):
    #suggestion_field = forms.CharField(validators=[must_be_caps]
    chirp_field = forms.CharField(label='Chirp:',
                                  max_length=240,
                                  widget=forms.TextInput(attrs={'class':'textInput'}))

class CommentForm(forms.Form):
    comment_field = forms.CharField(label='Comment:',
                                    max_length=240,
                                    widget=forms.TextInput(attrs={'class':'textInput'}))

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True
        )

    class Meta:
        model = User
        fields = ("username", "email",
                  "password1", "password2")

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
