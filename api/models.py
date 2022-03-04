from django.db import models


class Coin(models.Model):
    name = models.CharField(max_length=100, verbose_name='Coin')
    ticker = models.CharField(max_length=100, verbose_name='Ticker')

    class Meta:
        db_table = 'coin'


class Exchange(models.Model):
    exchange_symbol = models.CharField(max_length=100, verbose_name='Exchange symbol')
    display_symbol = models.CharField(max_length=100, verbose_name='Display symbol')
    exchange_name = models.CharField(max_length=200, verbose_name='Exchange name')
    color = models.CharField(max_length=100, verbose_name='Color')

    class Meta:
        db_table = 'exchange'


class Coins_exchanges(models.Model):
    coin_id = models.ForeignKey(Coin, on_delete=models.CASCADE)
    exchange_id = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    coin_symbol = models.CharField(max_length=100)

    class Meta:
        db_table = 'coin_exchange'
