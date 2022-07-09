from django.db import models


class category(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)
    categ = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='gor')

    def __str__(self):
        return self.title


# Create your models here.
class product(models.Model):
    pic = models.ImageField(upload_to='image', null=True, blank=True)
    pic1 = models.ImageField(upload_to='image', null=True, blank=True)
    pic2 = models.ImageField(upload_to='image', null=True, blank=True)
    title = models.CharField(max_length=30)
    category1 = models.ForeignKey(category, on_delete=models.CASCADE, null=True, blank=True, related_name='gat')
    price = models.IntegerField()
    discripion = models.CharField(max_length=300)
    slug = models.SlugField(max_length=30)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Opinion(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    title = models.CharField(max_length=50)
    text_area = models.TextField(max_length=300)
    proda=models.IntegerField(null=True)

    def __str__(self):
        return self.title
