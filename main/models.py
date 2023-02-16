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


class ClientFeedback(models.Model):
    name = models.CharField("Имя", max_length=100)
    feedback = models.TextField("Отзыв")
    # img = models.ImageField(upload_to='image')

    def __str__(self):
        return self.name         


class Deal(models.Model):
    banner = models.CharField(max_length=255)
    desc = models.TextField()        

    def __str__(self):
        return self.banner 


class HouseSale(models.Model):
    banner = models.CharField(max_length=255)
    desc = models.TextField()
    img = models.ImageField(upload_to='posts/')

    def __str__(self):
        return self.banner


class HousePost(models.Model):
    banner = models.CharField(max_length=200)
    desc = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts')
    price = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.banner
