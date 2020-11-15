from django.db import models


class Dentist(models.Model):
    name = models.TextField()
    location = models.TextField()
    specialization = models.TextField()

    def __str__(self):
        return f'{self.name} ({self.specialization}) in {self.location}'
