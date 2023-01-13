from django.db import models



class Banner(models.Model):
    banner = models.TextField(verbose_name='Название банера')

    def __str__(self):
        return self.banner


class AboutApartment(models.Model):
    about = models.TextField(verbose_name='О нашей квартире')
    desc = models.TextField()

    def __str__(self):
        return self.about 


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    number = models.IntegerField()
    message = models.TextField()
    
    def str(self):
        return self.message