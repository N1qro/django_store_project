from django.db import models


class AbstractItemDescriptorModel(models.Model):
    name = models.CharField(max_length=150)
    is_published = models.BooleanField(default=True)

    class Meta:
        abstract = True
