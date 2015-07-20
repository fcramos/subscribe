from django.test import TestCase
from ..forms import SubscriptionForm


class SubscriptionFormTest(TestCase):

    def test_form_fields(self):
        'Form should 9 fields'
        form = SubscriptionForm()
        self.assertCountEqual(
            [
                'name',
                'email',
                'html_level',
                'css_level',
                'js_level',
                'py_level',
                'dj_level',
                'ios_level',
                'android_level'
            ],
            form.fields
        )

    def test_validate(self, **kwargs):
        data = dict(
            name='Felipe Ramos',
            email='felipe@ramos.com',
            html_level=7,
            css_level=8,
            js_level=7,
            py_level=6,
            dj_level=8,
            ios_level=2,
            android_level=3
        )
        data.update(kwargs)
        form = SubscriptionForm(data)
        self.assertEqual(form.is_valid(), True)