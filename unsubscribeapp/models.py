from django.db import models

# Create your models here.
class Unsubscribe(models.Model):
    email = models.CharField(max_length=122)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self) -> str:
        return self.email