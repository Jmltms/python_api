from django.core.management.base import BaseCommand
from core import models as core_models
from django.db import transaction
import json


class Command(BaseCommand):
    help = "Upload stock data"

    def handle(self, *args, **options):
        file = open(
            'core/management/json/stock.json'
        ).read()
        json_data = json.loads(file)

        for data in json_data:
            with transaction.atomic():
                user = core_models.UserInfo.objects.filter(
                    first_name=data.get("first_name"),
                    last_name=data.get("last_name")
                ).first()

                stock = core_models.UserStock(
                    user=user,
                    stock_holder=data.get("stock_holder"),
                    invested=data.get("invested"),
                    stock_value=data.get("stock_value")
                )
                stock.save()

        print("stock uploaded successfully")
