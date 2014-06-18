from django import forms


class UploadFileForm(forms.Form):
    uploadedfile = forms.FileField(label='Select a file')