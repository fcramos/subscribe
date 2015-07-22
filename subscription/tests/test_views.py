# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r


class SubscriptionViewTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('home'))

    def test_get(self):
        'GET may result in 200.'
        self.assertEqual(200, self.response.status_code)

    def test_html(self):
        'Check is the form was rendered.'
        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 10)