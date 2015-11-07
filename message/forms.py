from django import forms 

from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('titre','auteur','sujet','mail','contenu')