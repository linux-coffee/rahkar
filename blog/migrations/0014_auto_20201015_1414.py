# Generated by Django 3.1.1 on 2020-10-15 14:14

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20201015_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='created',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='updated',
            field=django_jalali.db.models.jDateTimeField(auto_now=True),
        ),
    ]