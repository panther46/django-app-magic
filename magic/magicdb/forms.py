from django import forms

class Card_action(forms.Form):
    card_number = forms.BooleanField()

class Check(forms.Form):
    card_numbers= forms.CharField(max_length=500)
