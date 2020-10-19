from django.db import models

# Create your models here.
class Catagory(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    class Meta:
        verbose_name_plural = 'catagories'


    def __str__(self):
        return self.title


class Product(models.Model):
    catagory = models.ForeignKey(Catagory, related_name="Products", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()

    def __str__(self):
        return self.title