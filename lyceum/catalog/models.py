from django.core import validators
from django.core import exceptions
from django.db import models
from core.models import AbstractItemDescriptorModel


def ItemDescriptionValidator(value):
    lower_text = value.lower()
    if not ("превосходно" in lower_text or "роскошно" in lower_text):
        raise exceptions.ValidationError(
            "Описание не содержит в себе слов 'Роскошно' или 'Превосходно'"
        )


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


class Tag(AbstractItemDescriptorModel):
    slug = models.SlugField(
        unique=True,
        max_length=200,
        validators=(validators.validate_slug,))

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Item(AbstractItemDescriptorModel):
    text = models.TextField(
        verbose_name="Описание",
        help_text="Опишите объект",
        validators=[
            validators.MinLengthValidator(2),
            ItemDescriptionValidator,
        ],
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self) -> str:
        return self.name[:15]
