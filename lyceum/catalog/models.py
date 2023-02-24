from django.core import validators
from django.db import models

from catalog.validators import item_description_validator
from core.models import AbstractItemDescriptorModel, SlugMixin


class Category(AbstractItemDescriptorModel, SlugMixin):
    weight = models.SmallIntegerField(
        default=100,
        validators=(
            validators.MinValueValidator(0),
            validators.MaxValueValidator(32767)
        ),
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self) -> str:
        return self.name[:15]


class Tag(AbstractItemDescriptorModel, SlugMixin):
    class Meta:
        verbose_name = "тег"
        verbose_name_plural = "теги"

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
        verbose_name = "товар"
        verbose_name_plural = "товары"

    def __str__(self) -> str:
        return self.name[:15]
