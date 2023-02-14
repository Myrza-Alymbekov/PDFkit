from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    place_of_birth = models.CharField(max_length=15)
    image = models.ImageField(upload_to='avatar', blank=True, null=True, verbose_name='Photo')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Юзер'
        verbose_name_plural = 'Юзеры'



