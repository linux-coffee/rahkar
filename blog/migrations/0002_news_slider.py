# Generated by Django 3.1.1 on 2020-09-11 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='slider',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]