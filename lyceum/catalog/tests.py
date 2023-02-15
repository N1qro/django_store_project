from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_catalog_default_endpoint(self):
        responce = Client().get("/catalog/")
        self.assertEqual(responce.status_code, 200)

    def test_catalog_true_int_converter_endpoint(self):
        responce = Client().get("/catalog/13")
        self.assertEqual(responce.status_code, 200)

    def test_catalog_false_int_converter_endpoint(self):
        responce = Client().get("/catalog/13d")
        self.assertNotEqual(responce.status_code, 200)
