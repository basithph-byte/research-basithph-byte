from django.db import models

# Create your models here.
class List(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ListItem(models.Model):
    list = models.ForeignKey(List, related_name='items', on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)

    def __str__(self):
        return self.item_name