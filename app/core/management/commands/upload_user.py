from django.core.management.base import BaseCommand
from core import models as core_models
from django.db import transaction
import json


class Command(BaseCommand):
    help = "Upload user data"

    def handle(self, *args, **options):
        file = open(
            'core/management/json/user.json'
        ).read()
        json_data = json.loads(file)

        for data in json_data:
            with transaction.atomic():
                user = core_models.UserInfo(
                    first_name=data.get("first_name"),
                    last_name=data.get("last_name"),
                    address=data.get("address")
                )
                user.save()
                print(
                    f"{data.get('first_name')}"
                    f" {data.get('last_name')} successfully uploaded."
                )
