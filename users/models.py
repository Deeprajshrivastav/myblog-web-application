from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, ** kwargs):
        super().save(*args, **kwargs)  # saving image first

        img = Image.open(self.image.path)  # Open image using self

        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.image.path)  # saving image at the same path


class About(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    About = models.TextField(default='About')

    def __str__(self):
        return f'{self.user.username} About'

    def save(self, ** kwargs):
        super().save()

