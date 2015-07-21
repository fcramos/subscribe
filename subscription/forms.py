# coding: utf-8
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail


def send(destination, theme=''):
    """
    Function to send message by registered email
    """
    title = 'Obrigado por se candidatar'
    message = """
    Obrigado por se candidatar, assim que tivermos uma vaga disponível
    para programador %s entraremos em contato.
    """ % theme
    send_mail(
        subject=title,
        message=message,
        from_email='Vagas<vagas@meuspedidos.com.br>',
        recipient_list=[destination]
    )


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

    def send(self):
        """
        According knowledge, send email if bigger than 6
        """
        data = self.cleaned_data
        if data['html_level'] > 6 and data['css_level'] > 6 and data['js_level'] > 6:
            send(data['email'], 'Front-End')
        if data['py_level'] > 6 and data['dj_level'] > 6:
            send(data['email'], 'Back-end')
        if data['ios_level'] > 6 or data['android_level'] > 6:
            send(data['email'], 'Mobile')

        if data['html_level'] < 7 and data['css_level'] < 7 and data['js_level'] < 7 \
                and data['py_level'] < 7 and data['dj_level'] < 7 and data['ios_level'] < 7 and data['android_level'] < 7:
            send(data['email'])

        return data