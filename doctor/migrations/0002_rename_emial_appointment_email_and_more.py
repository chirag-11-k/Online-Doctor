# Generated by Django 4.2.4 on 2023-08-10 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='emial',
            new_name='email',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='accepted_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
