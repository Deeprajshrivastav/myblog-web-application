from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    dat_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    """ Enables users to comment on posts """
    commentator = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    date_added = models.DateTimeField(default=timezone.now)

    class meta:
        verbose_name_plural = 'comments'

    def __str__(self):
        return self.comment
