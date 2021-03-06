# Generated by Django 2.2.6 on 2019-11-13 18:35

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20191030_2109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='current_issue',
            new_name='other_issue',
        ),
        migrations.AddField(
            model_name='patient',
            name='issue',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Blood'), (2, 'Cancer'), (3, 'Cardiovascular/Heart'), (4, 'Ear'), (5, 'Eye'), (6, 'Infection'), (7, 'Immune'), (8, 'Injury/Accident'), (9, 'Mental Health'), (10, 'Metabolic/Endocrine'), (11, 'Muscle/Bone'), (12, 'Neurological'), (13, 'Oral and gastrointestinal'), (14, 'Renal and Urogenital'), (15, 'Reproduction/Childbirth'), (16, 'Respiratory'), (17, 'Skin'), (18, 'Stroke'), (19, 'General/Other')], default=1, max_length=47),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patient',
            name='severity',
            field=models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')]),
        ),
    ]
