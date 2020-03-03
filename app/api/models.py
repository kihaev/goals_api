from django.db import models


# Create your models here.


class Goal(models.Model):
    title = models.CharField(max_length=255)
    progress = models.FloatField()
    aligned_to = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
