from django import forms
from .models import BirthdayCard
from django.contrib.auth.models import User

class BirthdayCardForm(forms.ModelForm):
    class Meta:
        model = BirthdayCard
        fields = ['recipient', 'theme', 'color', 'emojis', 'message', 'scheduled_date']
        widgets = {
            'scheduled_date': forms.DateInput(attrs={'type': 'date', 'class': 'date-input'}),
            'message': forms.Textarea(attrs={'rows': 4, 'class': 'message-input'}),
            'emojis': forms.TextInput(attrs={'class': 'emoji-input'}),
        }
    
    recipient = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label="Recipient",
        widget=forms.Select(attrs={'class': 'recipient-select'})
    )