from django.test import SimpleTestCase
from django.urls import reverse

class TestSnickers(SimpleTestCase):

    def test_home_page(self):
        url = reverse('khome')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        url = reverse('khome')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'kitkathome.html')
        self.assertTemplateUsed(response, 'base.html') 

    def test_about_page(self):
        url = reverse('kabout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about_page_template(self):
        url = reverse('kabout')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'kitkatabout.html')
        self.assertTemplateUsed(response, 'base.html') 
