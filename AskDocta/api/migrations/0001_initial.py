# Generated by Django 2.2 on 2019-04-08 01:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('phonenumber', models.BigIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Enter your first name', max_length=30)),
                ('last_name', models.CharField(help_text='Enter your last name', max_length=30)),
                ('specialty', models.CharField(help_text='Enter your medical specialty (optional)', max_length=50)),
                ('gender', models.CharField(help_text='Enter your gender (optional)', max_length=30)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Enter your phone number (include country code)', max_length=128)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
