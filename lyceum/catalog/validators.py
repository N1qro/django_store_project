import django.core.exceptions


def item_description_validator(*words):
    def validator(value):
        lower_text = value.lower()
        if not any(word.lower() in lower_text for word in words):
            raise django.core.exceptions.ValidationError(
                f"Описание не содержит в себе слов: '{', '.join(words)}'"
            )

    return validator
