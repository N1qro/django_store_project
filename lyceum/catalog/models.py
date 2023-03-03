from django.core import validators
from django.db import models
# from sorl.thumbnail import get_thumbnail

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
        ],
    )

    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 null=True,
                                 verbose_name="Категория")
    tags = models.ManyToManyField(Tag, verbose_name="Тэги")
    main_picture = models.ImageField(upload_to="item_pictures",
                                     null=True,
                                     verbose_name="Главная картинка")
    cleanup_fields = ["main_picture"]
    cleanup_protection = True

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"

    def save(self, *args, **kwargs):
        if not self.id:
            super().save(*args, **kwargs)
            # resized = get_thumbnail(self.main_picture,
            #                         "300x300",
            #                         crop="center")
            # self.main_picture.save(self.main_picture.path,
            #                        resized.read(),
            #                        False)
        super().save(*args, **kwargs)

    def cleanup(self):
        self.main_picture.delete()

    def __str__(self) -> str:
        return self.name[:15]


class ItemPicture(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE,
                             related_name="item_pictures")
    picture = models.ImageField(upload_to="item_pictures",
                                verbose_name="Дополнительная картинка")

    class Meta:
        verbose_name = "изображение товара"
        verbose_name_plural = "изображения товаров"

    def __str__(self):
        l_slash_index = self.picture.name.index("/")
        image_name = self.picture.name[l_slash_index + 1:l_slash_index + 16]
        return f"Изображение {image_name}"
