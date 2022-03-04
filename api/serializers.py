from rest_framework import serializers

from models import *


class CoinSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, verbose_name='Coin')
    ticker = serializers.CharField(max_length=100, verbose_name='Ticker')

    class Meta:
        model = Coin
        fields = '__all__'


class ExchangeSerializer(serializers.Serializer):
    exchange_symbol = serializers.CharField(max_length=100, verbose_name='Exchange symbol')
    display_symbol = serializers.CharField(max_length=100, verbose_name='Display symbol')
    exchange_name = serializers.CharField(max_length=200, verbose_name='Exchange name')
    color = serializers.CharField(max_length=100, verbose_name='Color')

    class Meta:
        model = Exchange
        fields = '__all__'


class CoinsExchangesSerializer(serializers.Serializer):
    coin_id = serializers.RelatedField(source='coin', read_only=True)
    exchange_id = serializers.RelatedField(source='exchange', read_only=True)
    coin_symbol = serializers.CharField(max_length=100)

    class Meta:
        model = Coins_exchanges
        fields = '__all__'
