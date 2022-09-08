from django import forms

class EntryForm(forms.Form):
    name = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)

class EditForm(forms.Form):
    name = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)