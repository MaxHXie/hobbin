# Generated by Django 2.0.7 on 2018-07-11 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('external_page', '0003_auto_20180711_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='description',
            field=models.TextField(default=None, max_length=2048, null=True),
        ),
    ]