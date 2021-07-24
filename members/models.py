from django.db import models


# Create your models here.
class Members(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=13)
    school = models.TextField()

    class Meta:
        ordering = ['created']
