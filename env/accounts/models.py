from django.db import models

# Create your models here.


class Profile(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    phone = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    address = models.TextField()