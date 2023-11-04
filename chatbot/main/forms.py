from django import forms

class ChatForm(forms.Form):
    message = forms.CharField(label='You', max_length=100)
