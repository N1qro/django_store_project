from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_homepage_endpoint(self):
        responce = Client().get("/")
        self.assertEqual(responce.status_code, 200)
