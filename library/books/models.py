from django.db import models
from datetime import date

class booksModel(models.Model):
    book = models.CharField(max_length=255)
    data = models.DateField(default=date.today())
    days = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=255)

