from django.db import models
from utils.date_converter import to_string


# Create your models here.

class Token(models.Model):
    token = models.CharField(max_length=100)
    last_expiration = models.DateTimeField(null=True)

    def to_dict(self):
        if self.last_expiration is None:
            return {
                "id": self.id,
                "token": self.token
            }

        return {
            "id": self.id,
            "token": self.token,
            "last_expiration": to_string(self.last_expiration)
        }
