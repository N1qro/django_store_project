from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_coffee_endpoint(self):
        responce = Client().get("/coffee/")
        self.assertIn("Я чайник", responce.content.decode("UTF-8"))
        self.assertEqual(responce.status_code, 418)
