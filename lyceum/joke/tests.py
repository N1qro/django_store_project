from django.test import Client, override_settings, TestCase


class StaticURLTests(TestCase):
    def test_coffee_endpoint(self):
        responce = Client().get("/coffee/")
        self.assertIn("Я чайник", responce.content.decode("UTF-8"))
        self.assertEqual(responce.status_code, 418)

    @override_settings(MIDDLEWARE_CLASSES=(
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "joke.middleware.reverse_response.ResponseReverser"
    ), ENABLE_COFFEE_MIDDLEWARE=True)
    def test_coffee_middleware(self):
        client = Client()
        cached_data = set()
        for i in range(10):
            response = client.get("/coffee/")
            state = "Я чайник" in response.content.decode("UTF-8")
            cached_data.add(state)

        self.assertEqual(len(cached_data), 2)

    @override_settings(MIDDLEWARE_CLASSES=(
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "joke.middleware.reverse_response.ResponseReverser"
    ), ENABLE_COFFEE_MIDDLEWARE=False)
    def test_coffee_middleware_disabling(self):
        client = Client()
        cached_data = set()
        for i in range(10):
            response = client.get("/coffee/")
            state = "Я чайник" in response.content.decode("UTF-8")
            print(state)
            cached_data.add(state)

        self.assertEqual(len(cached_data), 1)
