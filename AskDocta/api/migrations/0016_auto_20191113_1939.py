# Generated by Django 2.2.6 on 2019-11-13 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20191113_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='start',
            field=models.DateField(blank=True, null=True),
        ),
    ]
