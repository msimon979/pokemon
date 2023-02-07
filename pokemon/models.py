from django.db import models


# Create your models here.
class Pokemon(models.Model):
    class Meta:
        constraints = [models.UniqueConstraint(fields=["name"], name="unique_name")]

    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=100, null=False)
    type_1 = models.TextField(max_length=20, null=True)
    type_2 = models.TextField(max_length=20, null=True)
    total_stats = models.IntegerField(null=True)
    hp = models.IntegerField(null=True)
    attack = models.IntegerField(null=True)
    defense = models.IntegerField(null=True)
    special_atk = models.IntegerField(null=True)
    special_def = models.IntegerField(null=True)
    speed = models.IntegerField(null=True)
    generation = models.IntegerField(null=True)
    legendary = models.BooleanField(null=True)
