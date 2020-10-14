from django.contrib.auth.models import AbstractUser
from django.db import models
from taggit.managers import TaggableManager


class User(AbstractUser):
    is_company_admin = models.BooleanField(default=False, verbose_name='Company admin')
    tags = TaggableManager()
