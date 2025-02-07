from django import forms

class UpperCaseCharField(forms.CharField):
    def to_python(self, value):
        return value.upper()