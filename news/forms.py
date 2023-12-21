from django import forms
from django.core.exceptions import ValidationError

from .models import News


class NewsForm(forms.ModelForm):
    description = forms.CharField(min_length=20)
    title = forms.CharField(required=False)
    autor = forms.CharField(required=False)
    date = forms.DateField(required=False)

    class Meta:
        model = News
        fields = ['name', 'description', 'quantity']

    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get("description")
        name = cleaned_data.get("name")

        if name == description:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data