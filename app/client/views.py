from rest_framework import (
    viewsets,
    status
)
from rest_framework.decorators import action
from rest_framework.response import Response
from client import serializers as client_serializer
from core import models as core_model
from django.db import transaction


class ClientView(viewsets.ModelViewSet):

    @action(methods=['POST'], detail=False)
    def place_order(self, request, pk=None):
        """
        <POST> url: /api/client/place_order/
        request = {
            "user_id": 1,
            "product": [
                {
                "id": 2,
                "quantity: 3
                },
                {
                "id": 3,
                "quantity: 2
                },
            ]
        }
        """
        data = request.data
        print(data)

        user_info = core_model.UserInfo.objects.filter(
            id=data.get("user_id")
        ).first()

        if not user_info:
            return Response(
                {
                    "success": False,
                    "message": "user doest not exist",
                }, status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
            for product in data.get('product'):
                prouduct_info = core_model.Product.objects.filter(
                    id=product.get("id")
                ).first()

                if not prouduct_info:
                    return Response(
                        {
                            "success": False,
                            "message": "product doest not exist",
                        }, status=status.HTTP_400_BAD_REQUEST)

                if prouduct_info.stock_on_hand > product.get('quantity'):
                    total_price = prouduct_info.price * product.get('quantity')
                    remaining_qty = (
                        prouduct_info.stock_on_hand - product.get('quantity')
                    )
                    transaction_order = core_model.Transaction(
                        product=prouduct_info,
                        user=user_info,
                        quantity=product.get('quantity'),
                        total=total_price
                    )
                    transaction_order.save()

                    prouduct_info.stock_on_hand = remaining_qty
                    prouduct_info.save()

                else:
                    return Response(
                        {
                            "success": False,
                            "message":
                            "insufficient product quantity may occur",
                        }, status=status.HTTP_400_BAD_REQUEST)

        return Response(
            {
                "success": True,
                "message": "Place order successfully",
            }, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['GET'], detail=False)
    def fetch_stock(self, request, pk=None):
        """
        <GET> url: api/client/fetch_stock/?user=1
        """

        user = self.request.query_params.get("user")
        user_info = core_model.UserStock.objects.filter(
            user__id=user
        )

        return Response({
            "success": True,
            "data": client_serializer.UserStockSerializer(
                instance=user_info,
                many=True
            ).data,
        }, status=status.HTTP_200_OK)
