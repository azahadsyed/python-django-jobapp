from django import forms

from subscribe.models import Subscribe
from django.utils.translation import gettext_lazy as _
# Custom validator to check for commas


def validate_comma(value):
    if "," in value:
        raise forms.ValidationError("Invalid value: commas are not allowed.")
    return value


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        # fields = ['firstName', 'lastName', 'emailId']
        fields = '__all__'
        # exclude = ('firstName',)
        labels = {'firstName': _('Enter First Name : '), 'lastName': _(
            'Enter Last Name : '), 'emailId': _('Enter Email ID : ')}
        # help_texts = {'firstName': _('Enter Characters Only'),     }

        error_messages = {
            'firstName': {
                'required': ' you can not move forward without First Name'
            }
        }
        # firstName = forms.CharField(max_length=30, label="Enter First Name : ", help_text="Enter characters only")
        # lastName = forms.CharField(max_length=30,  validators=[validate_comma], label="Enter Last Name : ")
        # emailId = forms.EmailField(max_length=30,  validators=[validate_comma], label="Enter Email ID: ")

        # Validation for first name
        def clean_firstName(self):
            data = self.cleaned_data['firstName']
            if "," in data:
                raise forms.ValidationError(
                    "Invalid First Name: commas are not allowed.")
            return data

        # Validation for last name
        def clean_lastName(self):
            data = self.cleaned_data['lastName']
            if "," in data:
                raise forms.ValidationError(
                    "Invalid Last Name: commas are not allowed.")
            return data

        # Validation for email
        def clean_emailId(self):
            data = self.cleaned_data['emailId']
            if "," in data:
                raise forms.ValidationError(
                    "Invalid Email ID: commas are not allowed.")
            return data
