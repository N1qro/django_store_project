from django.core import exceptions
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase
from parameterized import parameterized

from catalog import models


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


class ModelTests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        cls.category = models.Category.objects.create(
            is_published=True,
            name="Тест категория",
            slug="category-test-slug",
            weight=100,
        )

        cls.tag = models.Tag.objects.create(
            is_published=True,
            name="Тест тег",
            slug="tag-test-slug"
        )

    def tearDown(self) -> None:
        super().tearDown()
        models.Item.objects.filter(
            name=self.item.name
        ).delete()

    @parameterized.expand([
        ("1", exceptions.ValidationError),
        ("Описание без нужных слов", exceptions.ValidationError)
    ])
    def test_validators(self, text, excepted_exception):
        item_count = models.Item.objects.count()
        with self.assertRaises(excepted_exception):
            self.item = models.Item(
                name="Тест товар",
                category=self.category,
                text=text
            )
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(self.tag)
            self.item.save()

        self.assertEqual(models.Item.objects.count(), item_count)

    def test_item_creation(self):
        item_count = models.Item.objects.count()

        test_image = SimpleUploadedFile("test_image.png",
                                        b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR"
                                        b"\x00\x00\x00\x01\x00\x00\x00\x01\x08"
                                        b"\x02\x00\x00\x00\x90s\xdb\xee\x00\x00"
                                        b"\x00\x06PLTE\xff\xff\xff\xff\xff\xff"
                                        b"\x00\x00\x00\x04IDATx\x9c\xec\xff\x0f"
                                        b"\x00\x01\x01\x01\x01\x00\x9a\x18\xbf"
                                        b"\x00\x00\x00\x00IEND\xaeB`\x82")

        self.item = models.Item(
            name="Тестовое имя товара 1",
            category=self.category,
            text="Хорошее, длинное описание. Роскошно",
            main_picture=test_image,
        )
        self.item.full_clean()
        self.item.save()
        self.item.tags.add(self.tag)
        self.item.save()

        self.assertEqual(models.Item.objects.count(), item_count + 1)
        self.item.main_picture.delete(True)
