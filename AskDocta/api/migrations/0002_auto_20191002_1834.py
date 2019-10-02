# Generated by Django 2.2 on 2019-10-02 18:34

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.TextField()),
                ('lastName', models.TextField()),
                ('DOB', models.DateField()),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('currentIssue', models.TextField()),
                ('lengthOfIssue', models.TextField()),
                ('recentChanges', models.TextField()),
                ('allergies', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='doctor',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='gender',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='(include country code)', max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialty',
            field=models.CharField(max_length=50),
        ),
    ]
