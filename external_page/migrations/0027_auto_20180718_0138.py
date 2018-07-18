# Generated by Django 2.0.7 on 2018-07-18 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('external_page', '0026_instructor_city_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='price_model',
            field=models.CharField(choices=[('H', 'Per timme'), ('T', 'Per tillfälle'), ('X', 'Per timme och per person'), ('Y', 'Per tillfälle och per person')], default='H', max_length=1, null=True),
        ),
    ]
