# Generated by Django 4.0.10 on 2024-04-08 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_client_phone_num_alter_client_tel_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leadowner',
            name='date_completed',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='leadowner',
            name='date_transfer',
            field=models.DateField(blank=True, null=True),
        ),
    ]
