from django import forms
from .models import Order


class MakePaymentForm(forms.Form):
    MONTH_CHOICES = 