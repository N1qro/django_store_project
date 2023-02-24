from django.test import Client, TestCase
from parameterized import parameterized


class StaticURLTests(TestCase):
    def test_catalog_default_endpoint(self):
        responce = Client().get("/catalog/")
        self.assertEqual(responce.status_code, 200)

    @parameterized.expand([
        ("correct_int", 13, 200),
        ("incorrect_int", "13d", 404)
    ])
    def test_catalog_int_converter_endpoint(self, name, test_input, expected):
        client = Client()
        response = client.get(f"/catalog/{test_input}")
        self.assertEqual(response.status_code, expected)

    @parameterized.expand([
        (3, 200), (14, 200), (5252, 200), (987, 200),
        (0, 404), (-51, 404), (3.01, 404), ("d3", 404)
    ])
    def test_catalog_re_endpoint(self, test_input, expected):
        client = Client()
        response = client.get(f"/catalog/converter/{test_input}")
        self.assertEqual(response.status_code, expected)

    @parameterized.expand([
        (55123, 200), (1, 200), (99999999999999999999, 200),
        (0, 404), (-34344322, 404), (3.14, 404), ("h3", 404)
    ])
    def test_catalog_custom_converter(self, test_input, expected):
        client = Client()
        response = client.get(f"/catalog/re/{test_input}")
        self.assertEqual(response.status_code, expected)
