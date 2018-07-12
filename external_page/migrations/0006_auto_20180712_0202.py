# Generated by Django 2.0.7 on 2018-07-12 02:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('external_page', '0005_auto_20180711_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='instructor',
            name='city',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='zip_code',
            field=models.CharField(max_length=10),
        ),
    ]
