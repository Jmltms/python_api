# Generated by Django 4.0.10 on 2024-04-17 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_leadinformation_status_label'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leadowner',
            name='date_handle',
        ),
        migrations.RemoveField(
            model_name='leadowner',
            name='date_transfer',
        ),
        migrations.AlterField(
            model_name='leadowner',
            name='status',
            field=models.IntegerField(choices=[(1, 'on progress'), (2, 'done deal')], default=1),
        ),
        migrations.CreateModel(
            name='OwnerHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'active'), (2, 'inactive')], default=1)),
                ('date_handle', models.DateField(auto_now_add=True)),
                ('date_transfer', models.DateField(blank=True, null=True)),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.account')),
                ('lead_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.leadowner')),
            ],
        ),
    ]
