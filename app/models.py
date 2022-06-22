from django.db import models
from django.contrib.auth.models import User
import datetime


class Neighborhood(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    occupants_count = models.IntegerField(default=0)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Contacts(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    unit = models.CharField(max_length=100, blank=True, null=True)
    m_number = models.IntegerField(default=0)
    hood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Profile(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='media/default2.png', upload_to='media/', null=True, blank=True)
    neighborhood = models.ForeignKey(Neighborhood, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username)


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    posted_at = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)


class Business(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, null=True, blank=True, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)