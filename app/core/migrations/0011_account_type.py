# Generated by Django 4.0.10 on 2024-04-12 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_leadinformation_date_close_deal_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='type',
            field=models.IntegerField(blank=True, choices=[(1, 'manager'), (2, 'staff'), (3, 'external'), (4, 'admin')], null=True),
        ),
    ]
