# coding: utf-8
from django import forms
from django.utils.translation import ugettext_lazy as _


class SubscriptionForm(forms.Form):
    """
    Defining form to subscription
    """
    name = forms.CharField(label=_('Nome'), max_length=200, required=True, )
    email = forms.EmailField(label=_('Email'), required=True, )
    html_level = forms.IntegerField(label=_('HTML'), min_value=0, max_value=10, required=False, )
    css_level = forms.IntegerField(label=_('CSS'), min_value=0, max_value=10, required=False, )
    js_level = forms.IntegerField(label=_('JavaScript'), min_value=0, max_value=10, required=False, )
    py_level = forms.IntegerField(label=_('Python'), min_value=0, max_value=10, required=False, )
    dj_level = forms.IntegerField(label=_('Django'), min_value=0, max_value=10, required=False, )
    ios_level = forms.IntegerField(label=_('Desenvolvimento iOS'), min_value=0, max_value=10, required=False, )
    android_level = forms.IntegerField(label=_('Desenvolvimento Android'), min_value=0, max_value=10, required=False, )