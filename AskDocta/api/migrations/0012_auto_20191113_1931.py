# Generated by Django 2.2.6 on 2019-11-13 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20191113_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='issue',
            field=models.CharField(choices=[(1, 'Blood'), (2, 'Cancer'), (3, 'Cardiovascular/Heart'), (4, 'Ear'), (5, 'Eye'), (6, 'Infection'), (7, 'Immune'), (8, 'Injury/Accident'), (9, 'Mental Health'), (10, 'Metabolic/Endocrine'), (11, 'Muscle/Bone'), (12, 'Neurological'), (13, 'Oral and gastrointestinal'), (14, 'Renal and Urogenital'), (15, 'Reproduction/Childbirth'), (16, 'Respiratory'), (17, 'Skin'), (18, 'Stroke'), (19, 'General/Other')], max_length=2),
        ),
    ]