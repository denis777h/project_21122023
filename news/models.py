from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse

# Create your models here.




class News(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )
    description = models.TextField()
    quantity = models.IntegerField(
        validators=[MinValueValidator(0)]
    )

    def __str__(self):
        return f'{self.name.title()}: {self.description[:10]}'

    def get_absolute_url(self):
        return reverse('news', args=[str(self.id)])
    



