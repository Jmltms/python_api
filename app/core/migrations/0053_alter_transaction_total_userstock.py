# Generated by Django 4.2.16 on 2024-11-04 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0052_rename_prouct_code_product_product_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='total',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='UserStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_holder', models.CharField(blank=True, max_length=255, null=True)),
                ('invested', models.IntegerField(blank=True, null=True)),
                ('stock_value', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.userinfo')),
            ],
        ),
    ]
