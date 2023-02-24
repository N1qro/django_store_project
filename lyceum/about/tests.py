from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_about_endpoint(self):
        responce = Client().get("/about/")
        self.assertEqual(responce.status_code, 200)
