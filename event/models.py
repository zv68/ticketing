from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=256)
    date = models.DateField()
    place = models.CharField(max_length=256)
    price = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date', 'name', 'place']

    def __str__(self):
        return self.name
