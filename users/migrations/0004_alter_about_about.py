# Generated by Django 3.2.4 on 2021-06-21 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_describe_about_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='About',
            field=models.TextField(default='About'),
        ),
    ]