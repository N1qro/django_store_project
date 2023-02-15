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
        response1 = client.get("/catalog/re/3")
        response2 = client.get("/catalog/re/0")
        response3 = client.get("/catalog/re/-51")
        response4 = client.get("/catalog/re/3.01")
        response5 = client.get("/catalog/re/d3")
        self.assertEqual(response1.status_code, 200)
        self.assertNotEqual(response2.status_code, 200)
        self.assertNotEqual(response3.status_code, 200)
        self.assertNotEqual(response4.status_code, 200)
        self.assertNotEqual(response5.status_code, 200)

    def test_catalog_custom_converter(self):
        client = Client()
        response1 = client.get("/catalog/re/55123")
        response2 = client.get("/catalog/re/0")
        response3 = client.get("/catalog/re/-34344322")
        response4 = client.get("/catalog/re/3.14")
        response5 = client.get("/catalog/re/h3")
        self.assertEqual(response1.status_code, 200)
        self.assertNotEqual(response2.status_code, 200)
        self.assertNotEqual(response3.status_code, 200)
        self.assertNotEqual(response4.status_code, 200)
        self.assertNotEqual(response5.status_code, 200)
