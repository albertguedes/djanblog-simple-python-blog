# djanblog/tests/views/contact_view_test.py
from django.test import TestCase
from django.urls import reverse
from djanblog.views.contact import ContactForm

class ContactViewTest(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse('contact'))

    def test_contact_view_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_contact_view_template(self):
        self.assertTemplateUsed(self.response, 'contact.html')

    def test_contact_view_contains_form(self):
        self.assertContains(self.response, '<form')
        self.assertContains(self.response, 'name="email"')
        self.assertContains(self.response, 'name="name"')
        self.assertContains(self.response, 'name="subject"')
        self.assertContains(self.response, 'name="message"')

    def test_contact_view_context(self):
        self.assertIsInstance(self.response.context['form'], ContactForm)  # Use ContactForm diretamente
