# Generated by Django 2.0.7 on 2018-07-29 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobby_event', '0022_hobbyeventsignup_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobbyeventsignup',
            name='telephone',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
