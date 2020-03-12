from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class UserMaster(AbstractUser):
    flickr_id = models.CharField(max_length=30, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True, default=None)

    def __str__(self):
        return "%s. %s %s" % (self.id, self.first_name, self.last_name)
