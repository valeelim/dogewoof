from django.test import TestCase

# Create your tests here.
class APITest(TestCase):
    def test_contact_us(self):
        response = self.client.post('/contact-us/')
        self.assertEqual(response.url, '/authentication/login/?next=/contact-us/')

    def test_make_donation(self):
        response = self.client.post('/make-donation/')
        self.assertEqual(response.url, '/authentication/login/?next=/make-donation/')
    
    def test_homepage(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)