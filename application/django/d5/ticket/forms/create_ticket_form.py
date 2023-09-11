from django import forms


class CreateTicketForm(forms.Form):
    subject = forms.CharField(widget=forms.Textarea, required=True)
