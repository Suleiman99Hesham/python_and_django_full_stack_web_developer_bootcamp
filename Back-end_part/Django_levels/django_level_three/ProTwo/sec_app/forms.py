from django import forms
from sec_app.models import User
    
class Register(forms.ModelForm):
    verify_email = forms.CharField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean(self):
        email = self.cleaned_data["email"]
        v_email = self.cleaned_data["verify_email"]
        if email != v_email:
            raise forms.ValidationError("verfication email is not correct")
    

# class Register(forms.Form):
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     email = forms.EmailField()