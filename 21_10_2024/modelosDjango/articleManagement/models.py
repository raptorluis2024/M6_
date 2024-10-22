from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length = 30)
    address = models.CharField(max_length = 30)
    price = models.IntegerField()
    category = models.CharField(max_length = 30)
    
    def clean(self):
        if not self.name:
            raise ValidationError("El nombre es obligatorio.")
        if self.price <= 0:
            raise ValidationError("El precio debe ser mayor que 0.")

    def save(self, *args, **kwargs):
        self.full_clean()
        #super().save(*args, **kwargs)
        super(Article,self).save(*args, **kwargs)