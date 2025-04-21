from django.db import models
from .category import Category
from .tag import Tag


class Promotion(models.Model):
    title = models.CharField(max_length=100)
    ssubtitle = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField()
    link = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.title
    
