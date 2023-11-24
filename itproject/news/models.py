from django.db import models

class Artiles(models.Model):
    date = models.DateField()
    tittle = models.CharField('name', max_length=50)
    anons = models.CharField('anons', max_length=250)
    full_text = models.TextField()
    date = models.DateTimeField('date publish')

    def __str__(self):
        return f'news: {self.tittle}'


class Meta:
    verbose_name = 'news'
    verbose_name_plural = 'news'
