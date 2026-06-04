from django import forms
from django.forms import TextInput, Textarea

from .models import status_choices


class TaskForm(forms.Form):
    title = forms.CharField(
        required=True,
        max_length=200,
        label="Title",
        widget=TextInput(attrs={"class": "form-control"})
    )

    description = forms.CharField(
        required=False,
        max_length=500,
        label="Description",
        widget=Textarea(attrs={"class": "form-control", "rows": "5"})
    )

    status = forms.ChoiceField(
        required=True,
        choices=status_choices,
        label="Status",
        widget=forms.Select(attrs={"class": "form-select"})
    )

    finish_date = forms.DateField(
        required=False,
        label="Finish Date",
        widget=forms.DateInput(attrs={
            "class": "form-control",
            "type": "date"
        })
    )