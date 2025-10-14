import uuid
from django.utils.translation import gettext_lazy as _
from django.db import models

class IdModel(models.Model):
    # use this for every new db entry
    id = models.UUIDField(
        _('id'),
        primary_key = True,
        default = uuid.uuid4
    )
    class Meta:
        abstract = True # can inherit from this model


