# Generated by Django 3.1.1 on 2020-10-15 14:10

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_contactus_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactus',
            options={'ordering': ('created',), 'verbose_name': 'تماس با ما', 'verbose_name_plural': 'تماس ها'},
        ),
        migrations.AlterField(
            model_name='news',
            name='created',
            field=django_jalali.db.models.jDateTimeField(),
        ),
    ]
