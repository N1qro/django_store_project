from django.core import validators
from django.db import models


class AbstractItemDescriptorModel(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")
    is_published = models.BooleanField(default=True,
                                       verbose_name="Опубликовано?")

    class Meta:
        abstract = True


class SlugMixin(models.Model):
    slug = models.SlugField(
        unique=True,
        max_length=200,
        validators=(validators.validate_slug,))

    class Meta:
        abstract = True
