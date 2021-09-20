from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100)
    asunto = forms.CharField(label='Asunto', max_length=100)
    texto = forms.CharField(widget=forms.Textarea)    
    
    