import json
import oandapyV20
import oandapyV20.endpoints.orders as orders
from exampleauth import exampleauth
import sys
#stoploss in pips
stoploss=sys.argv[1]
stoploss=float(stoploss)
dollarrisk=100
#one USD = 0.1 lots
units=int((dollarrisk/stoploss)*10000)

#print(type(units))
#print('UNITS:',units)

accountID, access_token = exampleauth.exampleAuth()
client = oandapyV20.API(access_token=access_token)


# create a market order to enter a LONG position 10000 EUR_USD, stopLoss @1.07 takeProfit @1.10 ( current: 1.055)
# according to the docs at developer.oanda.com the requestbody looks like:

mktOrder = {
  "order": {
    "timeInForce": "FOK",      # Fill-or-kill
    "instrument": "EUR_USD",
    "positionFill": "DEFAULT",
    "type": "MARKET",
    "units": units,            # as integer
  }
}
r = orders.OrderCreate(accountID=accountID, data=mktOrder)
try:
    rv = client.request(r)
except V20Error as err:
    print("V20Error occurred: {}".format(err))
else:
    print("Response: {}\n{}".format(r.status_code, json.dumps(rv, indent=2)))
#print("Request: ", r)
#print("MarketOrder specs: ", json.dumps(mktOrder, indent=2))