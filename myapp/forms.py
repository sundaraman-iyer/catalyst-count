from django import forms

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField(label="Choose a CSV file", widget=forms.FileInput(attrs={'accept': '.csv'}))
