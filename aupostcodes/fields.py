from django import forms
from django.db import models
from django.forms.fields import RegexField
from django.utils.translation import ugettext_lazy as _

from models import AUPostCode


class AUPostCodeFormField(RegexField):
    """Australian post code field."""
    default_error_messages = {
        'invalid': _('Enter a valid 4 digit post code.'),
    }

    def __init__(self, **kwargs):
        defaults = {
            'max_length': 4,
            'min_length': 4
        }
        defaults.update(kwargs)
        super(AUPostCodeFormField, self).__init__(r'^\d{4}$', **defaults)
        
    def clean(self, value):
        value = super(AUPostCodeFormField, self).clean(value)
        try:
            postcode = AUPostCode.objects.get(postcode=value)
        except AUPostCode.DoesNotExist:
            raise forms.ValidationError('Enter a valid post code')
        return value


class AUPostCodeField(models.CharField):
    def __init__(self, **kwargs):
        defaults = {
            'max_length': 4
        }
        defaults.update(kwargs)
        return super(AUPostCodeField, self).__init__(**defaults)
        
    def formfield(self, **kwargs):
        return AUPostCodeFormField(**kwargs)
