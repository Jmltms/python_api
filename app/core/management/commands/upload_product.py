from django.core.management.base import BaseCommand
from core import models as core_models
from django.db import transaction
import json


class Command(BaseCommand):
    help = "Upload product data"

    def handle(self, *args, **options):
        file = open(
            'core/management/json/product.json'
        ).read()
        json_data = json.loads(file)

        for data in json_data:
            with transaction.atomic():
                product = core_models.Product(
                    product_code=data.get("product_code"),
                    name=data.get("name"),
                    stock_on_hand=data.get("stock_on_hand"),
                    price=data.get("price"),
                    description=data.get("description")
                )
                product.save()
                print(f"{data.get('name')} successfully uploaded.")
