# Generated by Django 3.2.4 on 2021-06-21 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_about'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='describe',
            new_name='About',
        ),
    ]
