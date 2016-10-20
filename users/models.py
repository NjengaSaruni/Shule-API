from __future__ import unicode_literals
import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

   
class CustomUser(AbstractUser):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	created_at = models.DateTimeField(blank=True, auto_now_add=True)
	updated_at = models.DateTimeField(blank=True, auto_now=True)
