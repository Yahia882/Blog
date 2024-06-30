from .models import comment_section
from django import forms
class comment_form(forms.ModelForm):
    class Meta:
        model = comment_section
        exclude =["Post"]
        labels ={"comment":"Add Comment"}