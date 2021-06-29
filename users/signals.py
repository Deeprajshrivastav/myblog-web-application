from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, About


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=User)
def create_user_about(sender, instance, created, **kwargs):
    if created:
        About.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_about(sender, instance, **kwargs):
    instance.about.save()