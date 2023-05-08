from django import forms

class SortingForm(forms.Form):
    data = forms.CharField(label='Enter a list of numbers separated by commas', max_length=100) # type: ignore

    def clean_data(self):
        data = self.cleaned_data['data']
        # Custom validation or cleaning logic for the 'data' field
        return data