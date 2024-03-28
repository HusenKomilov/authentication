from django.db import models
from utils.models import BaseModel

    
class Book(BaseModel):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    level = models.CharField(max_length=255, null=True)
    category = models.CharField(max_length=255, null=True)
    language = models.CharField(max_length=16, null=True)

    number_of_pages = models.IntegerField()
    price = models.IntegerField(blank=True, null=True)
    published_at = models.IntegerField()
   
    is_discount = models.BooleanField(default=False)
    is_saved = models.BooleanField(default=False)

    image = models.ImageField(upload_to='media/')
    description = models.TextField()

    rating = models.FloatField()

    def __str__(self):
        return self.title

