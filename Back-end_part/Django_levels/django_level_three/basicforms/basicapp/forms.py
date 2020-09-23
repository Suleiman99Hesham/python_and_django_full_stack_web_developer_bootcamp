from django import forms
from django.core import validators

def check_for_s(name):
    if name[0].lower() != 's':
        raise forms.ValidationError('name must start with "s" ')

class FormName(forms.Form):
    name = forms.CharField(validators = [check_for_s])
    email = forms.EmailField()
    text = forms.CharField(widget = forms.Textarea)
    botcatcher = forms.CharField(required=False, widget = forms.HiddenInput,
                                    validators = [validators.MaxLengthValidator(0)])

    #ANOTHER METHOD FOR CLEANING NAME
    # def clean_name(self):
    #     name = self.cleaned_data["name"]
    #     if name[0].lower() != 's':
    #         raise forms.ValidationError('name must start with "s" ')