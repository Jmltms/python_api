# Generated by Django 4.2.16 on 2024-11-04 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0051_product_transaction_userinfo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='prouct_code',
            new_name='product_code',
        ),
    ]
