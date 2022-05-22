
import ccxt  

exchange = ccxt.bybit({
    'options': {
        'adjustForTimeDifference': True,
    },
    'apiKey': '*****apiKey*****',
    'secret': '*****secret*****',
    'password': '*****password*****',
})


print(exchange)


response = exchange.private_get_spot_v1_account()
print(response)
