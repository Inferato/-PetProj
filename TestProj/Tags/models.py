from django.db import models
from .User import User
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase


class Tagged(TaggedItemBase):
    parent = models.ForeignKey('self', on_delete=models.CASCADE)
