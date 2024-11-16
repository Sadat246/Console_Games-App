from django.db import models
from django.contrib.auth.models import User

from players.models import Player

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                primary_key=True)
    player = models.OneToOneField(Player, on_delete=models.CASCADE,
                                  blank=True, null=True)
    permissions_updated_at = models.DateTimeField()
    guid_password_reset = models.UUIDField(unique=True, null=True, blank=True)
    guid_password_expiry = models.DateTimeField(null=True, blank=True)