from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_catalog_default_endpoint(self):
        responce = Client().get("/catalog/")
        self.assertEqual(responce.status_code, 200)

    def test_catalog_int_converter_endpoint(self):
        client = Client()
        response1 = client.get("/catalog/13")
        response2 = client.get("/catalog/13d")
        self.assertEqual(response1.status_code, 200)
        self.assertNotEqual(response2.status_code, 200)

    def test_catalog_re_endpoint(self):
        client = Client()
        right_data = ["3", "14", "5252", "987"]
        wrong_data = ["0", "-51", "3.01", "d3"]

        for element in right_data:
            response = client.get(f"/catalog/converter/{element}")
            self.assertEqual(response.status_code, 200)

        for element in wrong_data:
            response = client.get(f"/catalog/converter/{element}")
            self.assertNotEqual(response.status_code, 200)

    def test_catalog_custom_converter(self):
        client = Client()
        right_data = ["55123", "1", "99999999999999"]
        wrong_data = ["0", "-34344322", "3.14", "h3"]

        for element in right_data:
            response = client.get(f"/catalog/re/{element}")
            self.assertEqual(response.status_code, 200)

        for element in wrong_data:
            response = client.get(f"/catalog/re/{element}")
            self.assertNotEqual(response.status_code, 200)
