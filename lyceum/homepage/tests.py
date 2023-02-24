from django.test import Client, override_settings, TestCase


class StaticURLTests(TestCase):
    def test_homepage_endpoint(self):
        response = Client().get("/")
        self.assertEqual(response.status_code, 200)

    def test_coffee_endpoint(self):
        response = Client().get("/coffee/")
        self.assertIn("Я чайник", response.content.decode("UTF-8"))
        self.assertEqual(response.status_code, 418)

    @override_settings(MIDDLEWARE_CLASSES=(
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "homepage.middleware.reverse_response.ResponseReverser"
    ), ENABLE_COFFEE_MIDDLEWARE=True)
    def test_coffee_middleware(self):
        client = Client()
        has_reversed = False
        for i in range(10):
            response = client.get("/coffee/")
            is_normal = "Я чайник" in response.content.decode("UTF-8")
            if not is_normal:
                has_reversed = True

        self.assertTrue(has_reversed)

    @override_settings(MIDDLEWARE_CLASSES=(
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "homepage.middleware.reverse_response.ResponseReverser"
    ), ENABLE_COFFEE_MIDDLEWARE=False)
    def test_coffee_middleware_disabling(self):
        client = Client()
        cached_data = set()
        for i in range(10):
            response = client.get("/coffee/")
            state = "Я чайник" in response.content.decode("UTF-8")
            cached_data.add(state)

        self.assertEqual(len(cached_data), 1)
