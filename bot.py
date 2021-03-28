import config
from binance.client import Client
from binance.enums import *
import time
import vlc
import threading
import math
import csv
import itertools
import datetime

client = Client(config.API_KEY, config.API_SECRET, tld='com')
symbolTicker = 'BTCUSDT'
symbolPrice = 0
ma20 = 0

dineroFinal = 0.0

ma20_local = 0
values = []
sum = 0
cantCompra = 0
cantVenta = 0
q = 0

klines = client.get_historical_klines(symbolTicker, Client.KLINE_INTERVAL_1HOUR, "10 year ago UTC")
print(len(klines))
for i in range(30,len(klines)):
    sum = 0
    prom = 0
    for j in range(i-20,i):
        sum = sum + float(klines[j][4])

    prom = sum / 20

    if ( float(klines[i][4]) < prom*0.99 and 0 <= q < 5):
        #compra
        #print("compra  " + str(klines[i][4]))
        q = q + 1
        cantCompra = cantCompra +1
        dineroFinal = dineroFinal - prom*0.99#*1.00075
        #time.sleep(1)
    if ( float(klines[i][4]) > prom*1.01 and 0 < q <= 5):
        #venta
        #print("venta  " + str(klines[i][4]))
        q = q - 1
        cantVenta = cantVenta +1
        dineroFinal = dineroFinal + prom*1.01#*0.99925
        #time.sleep(1)

print(dineroFinal)
print(cantCompra)
print(cantVenta)
