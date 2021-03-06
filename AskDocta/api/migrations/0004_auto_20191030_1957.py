# Generated by Django 2.2 on 2019-10-30 19:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0003_auto_20191002_1843'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllergyChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='FamHistChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='MedHistChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialty', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('is_doctor', models.BooleanField(default=False)),
                ('is_registrar', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='(include country code)', max_length=128, region=None)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='patient',
            name='length_of_issue',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='recent_changes',
        ),
        migrations.AddField(
            model_name='patient',
            name='alc',
            field=models.CharField(choices=[('N', 'None'), ('O', 'Occasional'), ('F', 'Frequent')], default=None, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='curr_meds',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='fam_other_hist',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='height',
            field=models.CharField(default=None, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='other_allergy',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='other_hist',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='severity',
            field=models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9')], default=None, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='smoke',
            field=models.CharField(choices=[('N', 'None'), ('F', 'Former'), ('S', 'Some Days'), ('M', 'Most/Every Day')], default=None, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='start',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='weight',
            field=models.CharField(default=None, max_length=30),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='patient',
            name='allergies',
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
        migrations.AddField(
            model_name='patient',
            name='fam_hist',
            field=models.ManyToManyField(to='api.FamHistChoice'),
        ),
        migrations.AddField(
            model_name='patient',
            name='med_hist',
            field=models.ManyToManyField(to='api.MedHistChoice'),
        ),
        migrations.AddField(
            model_name='patient',
            name='allergies',
            field=models.ManyToManyField(to='api.AllergyChoice'),
        ),
    ]
