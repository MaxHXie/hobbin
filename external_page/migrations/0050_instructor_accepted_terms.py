# Generated by Django 2.0.7 on 2018-07-28 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('external_page', '0049_auto_20180728_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='accepted_terms',
            field=models.BooleanField(default=True),
        ),
    ]
