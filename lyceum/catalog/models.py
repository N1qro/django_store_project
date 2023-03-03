from core.models import AbstractItemDescriptorModel
from django.core import exceptions
from django.core import validators
from django.db import models
from sorl.thumbnail import get_thumbnail
from django.core.files.base import ContentFile

from core.models import AbstractItemDescriptorModel, SlugMixin


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
        ],
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag)
    main_picture = models.ImageField(upload_to="item_pictures", null=True)
    cleanup_fields = ["main_picture"]
    cleanup_protection = True

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"

    def save(self, *args, **kwargs):
        if not self.id:
            super().save(*args, **kwargs)
            resized = get_thumbnail(self.main_picture, "300x300", crop="center")
            print("Moved here")
            self.main_picture.save(resized.name, ContentFile(resized.read()), False)
        print("Saved here")
        super().save(*args, **kwargs)

    def cleanup(self):
        self.main_picture.delete()

    def __str__(self) -> str:
        return self.name[:15]


class ItemPicture(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE,
                             related_name="item_pictures")
    picture = models.ImageField(upload_to="item_pictures")

    class Meta:
        verbose_name = "изображение товара"
        verbose_name_plural = "изображения товаров"
