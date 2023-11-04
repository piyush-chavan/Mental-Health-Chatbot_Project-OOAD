from django import forms

class ChatForm(forms.Form):
    message = forms.CharField(label='You', max_length=100,widget=forms.TextInput(attrs={'class': 'input-box'}))
