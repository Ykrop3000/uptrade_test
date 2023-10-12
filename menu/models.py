from django.db import models
from django.urls import reverse

#
# class Menu(models.Model):
#     title = models.CharField(max_length=100)
#

# Create your models here.
class MenuItem(models.Model):
    # menu = models.ForeignKey(Menu, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    url = models.CharField(max_length=200, default='', blank=True)
    named_url = models.CharField(max_length=100, null=True, blank=True)

    def get_url(self):
        if not self.named_url:
            return self.url
        else:
            return reverse(self.named_url)

    def __str__(self):
        return f'{self.title} -> {self.parent.title}' if self.parent else self.title
