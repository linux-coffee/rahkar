# Generated by Django 3.1.1 on 2020-10-15 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20201015_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='phone',
            field=models.CharField(max_length=20, null=True, verbose_name='تلفن تماس'),
        ),
    ]
