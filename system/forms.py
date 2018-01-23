from django import forms
from django.utils.translation import ugettext

name = ugettext(u'Имя')
number = ugettext(u'Телефон')


class FeedbackForm(forms.Form):
    first_name = forms.CharField(required=True, label=u' ', label_suffix=u' ',
                                 widget=forms.TextInput(attrs={'class': 'input', 'placeholder': name}))
    phone_number = forms.CharField(required=True, label=u' ', label_suffix=u' ',
                                   widget=forms.TextInput(attrs={'class': 'input', 'placeholder': number}))
