from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Card(models.Model):
    title=models.CharField(max_length=50)
    number=models.IntegerField(blank=True, null=True, unique=True)
    collection=models.CharField(max_length=50)
    kind=models.CharField(max_length=50)
    owned=models.BooleanField(default=False)
    image=models.ImageField(upload_to = 'magicdb/card_images',
                            default="magicdb/card_images/no-img.jpg")
    owned_by = models.ManyToManyField(User, related_name='cards')

    def __str__(self):
        return "%s - %s" %(self.number, self.title)
