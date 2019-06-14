from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User
GRADE_CHOICES = (
     (1, "1"),
     (2, "2"),
     (3, "3"),
     (4, "4"),
     (5, "5"),
 )

class Turnament(models.Model):
        name=models.CharField( max_length=64)
        place=models.CharField( max_length=64)
        description = models.CharField(max_length=120)
        date_start=models.DateField(null=True)
        date_end=models.DateField(null=True)
        price=models.IntegerField(null=True)
        user=models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

class Usertur(models.Model):
    user=models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    grade =models.CharField(choices=GRADE_CHOICES, max_length=5)
    tournament=models.ForeignKey(Turnament, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('user', 'tournament', 'grade')




