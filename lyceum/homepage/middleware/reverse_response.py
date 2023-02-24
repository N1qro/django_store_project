from django.conf import settings


class ResponseReverser:
    times_entered = 0

    def __init__(self, get_response) -> None:
        self.get_response = get_response
        self.enable_mid = settings.ENABLE_COFFEE_MIDDLEWARE

    def __call__(self, request):
        if self.enable_mid and request.path == "/coffee/":
            response = self.get_response(request)
            type(self).times_entered += 1
            if self.times_entered == 10:
                type(self).times_entered = 0
                response.content = self.reverse_words(response.content.split())
            return response
        else:
            return self.get_response(request)

    def reverse_words(self, strings):
        strings = map(self.transform_string, strings)
        return " ".join((word[::-1] for word in strings))

    def transform_string(self, string):
        return string.decode("UTF-8").strip("</body>")
