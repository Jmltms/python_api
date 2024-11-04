from rest_framework import serializers
from core import models as core_models


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = core_models.UserInfo
        fields = '__all__'


class ProuctSerializer(serializers.ModelSerializer):
    class Meta:
        model = core_models.Product
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = core_models.Transaction
        fields = '__all__'


class UserStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = core_models.UserStock
        fields = [
            'id',
            'user',
            'stock_holder',
            'invested',
            'stock_value'
        ]

    user = serializers.SerializerMethodField(
        'fetch_user'
    )

    def fetch_user(self, obj):
        return "%s %s" % (
            obj.user.first_name,
            obj.user.last_name
        )
