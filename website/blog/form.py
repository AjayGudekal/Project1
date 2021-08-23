from django import forms
from .models import EnqDB

class ContactForm(forms.Form):
    contact_name = forms.CharField(max_length=30, required=True)
    contact_email = forms.CharField(required=True)
    phno = forms.IntegerField()
    text = forms.CharField(widget=forms.Textarea())

class EnqDBForm(forms.ModelForm):
    class Meta :
        model=EnqDB
        fields=('name','mail','mno','messege')


from .models import Postlu

class Postform(forms.ModelForm):
    class Meta:
        model=Postlu
        fields=("author","title","text","created_date")














