from store.models import Product, Customer, Cart
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price']
        extra_kwargs = {
                'title': {
                    'validators': [
                        UniqueValidator(
                            queryset=Product.objects.all()
                        )
                    ]
                }
            }


class CustomerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Customer
        fields = ['id', 'user_id', 'first_name', 'last_name', 'phone']


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = Cart
        fields = ['id']