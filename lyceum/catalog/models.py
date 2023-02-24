from core.models import AbstractItemDescriptorModel
from django.core import exceptions
from django.core import validators
from django.db import models


def item_description_validator(*words):
    def validator(value):
        lower_text = value.lower()
        if not any(word.lower() in lower_text for word in words):
            raise exceptions.ValidationError(
                f"Описание не содержит в себе слов: '{', '.join(words)}'"
            )

    return validator


class Category(AbstractItemDescriptorModel):
    slug = models.SlugField(
        unique=True,
        max_length=200,
        validators=(validators.validate_slug,))
    weight = models.SmallIntegerField(
        default=100,
        validators=(
            validators.MinValueValidator(0),
            validators.MaxValueValidator(32767)
        ),
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self) -> str:
        return self.name[:15]


class Tag(AbstractItemDescriptorModel):
    slug = models.SlugField(
        unique=True,
        max_length=200,
        validators=(validators.validate_slug,))

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self) -> str:
        return self.name[:15]


class Item(AbstractItemDescriptorModel):
    text = models.TextField(
        verbose_name="Описание",
        help_text="Это описание увидит пользователь. Больше конкретики",
        validators=[
            validators.MinLengthValidator(2),
            item_description_validator("Роскошно", "Превосходно"),
        ],
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self) -> str:
        return self.name[:15]
