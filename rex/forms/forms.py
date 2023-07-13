from django import forms
from ..models import Contact

class Contact(forms.ModelForm):
	class Meta:
		model = Contact
		fields = '__all__'
	contact_id = forms.CharField(required=True)
	contact_date = forms.DateField(required=True)
	contact_phone = forms.CharField(required=True, max_length=20)
	contact_email = forms.CharField(required=True, max_length=100)
	contact_inquiry = forms.CharField(required=True, max_length=1000)
 
class Inquiry(forms.Form):
    contact_phone = forms.CharField(required=True, max_length=20)
    contact_email = forms.CharField(required=True, max_length=100)
    contact_inquiry = forms.CharField(required=True, max_length=1000)