# Generated by Django 4.0.10 on 2024-04-25 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_alter_activity_type_alter_client_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='TermStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('months', models.IntegerField(blank=True, choices=[(1, 'january'), (2, 'february'), (3, 'march'), (4, 'april'), (5, 'may'), (6, 'june'), (7, 'july'), (8, 'august'), (9, 'september'), (10, 'october'), (11, 'november'), (12, 'december')], null=True)),
                ('date_pay', models.DateField(blank=True, null=True)),
                ('date_unpay', models.DateField(blank=True, null=True)),
                ('status', models.IntegerField(blank=True, choices=[(1, 'paid'), (2, 'unpaid')], null=True)),
                ('lead_service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.leadservices')),
            ],
        ),
    ]
