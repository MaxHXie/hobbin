# Generated by Django 2.0.7 on 2018-07-25 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobby_event', '0014_auto_20180725_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobbyeventsignup',
            name='email',
            field=models.CharField(blank=True, max_length=64, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='hobbyeventsignup',
            name='telephone',
            field=models.CharField(blank=True, max_length=16, null=True, unique=True),
        ),
    ]
