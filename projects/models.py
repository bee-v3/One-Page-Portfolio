from django.db import models
from django.utils.text import slugify

class Project(models.Model):
    title = models.CharField(max_length=500)
    short = models.CharField(max_length=1000, default=None, blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)
    technology = models.CharField(max_length=500, blank=True, null=True)
    image = models.FilePathField(path='static/images/projects', default='default_user.png', blank=True, null=True)
    url = models.CharField(max_length=500,default=None, blank=True, null=True)
    demo = models.CharField(max_length=500,default=None, blank=True, null=True)
    slug = models.SlugField(max_length=500, unique=True)
    def __str__(self):
        return self.title

class LandingMessage(models.Model):
    name = models.CharField(max_length=500)
    header = models.CharField(max_length=300, default=None, blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)
    image = models.FilePathField(path='static/images/user', default='default_user.jpg', blank=True, null=True)
    def __str__(self):
        return self.name

    @classmethod
    def object(cls):
        return cls._default_manager.all().first()

    def save(self, *args, **kwargs):
        self.pk = self.id = 1
        return super().save(*args, **kwargs)