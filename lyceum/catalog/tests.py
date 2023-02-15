from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_catalog_default_endpoint(self):
        responce = Client().get("/")
        self.assertEqual(responce.status_code, 200)

    def test_catalog_int_converter_endpoint(self):
        responce = Client().get("/13")
        self.assertEqual(responce.status_code, 200)
