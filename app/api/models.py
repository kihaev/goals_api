from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Goal(models.Model):
    title = models.CharField(max_length=255)
    progress = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    aligned_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
