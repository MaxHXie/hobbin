# Generated by Django 2.0.7 on 2018-07-28 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobby_event', '0017_auto_20180728_1821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventzipcodesearch',
            name='user',
        ),
        migrations.AddField(
            model_name='eventsearch',
            name='zip_code_search',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.DeleteModel(
            name='EventZipCodeSearch',
        ),
    ]
