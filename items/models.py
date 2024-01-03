from django.db import models

from accounts.models import CustomUser

class Items(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    price = models.PositiveIntegerField(null=True)
    selling_price = models.PositiveIntegerField(null=True)
