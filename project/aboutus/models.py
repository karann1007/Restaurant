from django.db import models

# Create your models here.
class AboutUs(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    # image=models.ImageField(upload_to='aboutUs/')
    class Meta:
        verbose_name = 'AboutUs'
        verbose_name_plural = 'AboutUs'


    def __str__(self):
        return self.title
class WhyChooseUs(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()

    class Meta:
        verbose_name = 'WhyChooseUs'
        verbose_name_plural = 'WhyChooseUs'


    def __str__(self):
        return self.title


class Chef(models.Model):
    name=models.CharField(max_length=50)
    subtitle=models.CharField(max_length=50)
    bio=models.TextField()
    image=models.ImageField(upload_to='chef/')

    class Meta:
        verbose_name = 'Chef'
        verbose_name_plural = 'Chefs'


    def __str__(self):
        return self.name
