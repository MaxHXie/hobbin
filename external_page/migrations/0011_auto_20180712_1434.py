# Generated by Django 2.0.7 on 2018-07-12 14:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('external_page', '0010_auto_20180712_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]