import urllib.request
import json


def getStockData(symbol):
    URL = 'https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&symbols=' + symbol + '&apikey=DR0XFIONSG2PIK4A'
    connection = urllib.request.urlopen(URL)
    responseString = connection.read().decode()
    print (responseString)
    jsonRes = json.loads(responseString)
    print ("The current price of " + symbol + " is " + jsonRes['Stock Quotes'][0]['2. price'])
    print ("Stock Quotes retrieved successfully!")


def main():
    symbol = input('Stock Symbol:')
    while symbol != 'quit':
        getStockData(symbol)
        symbol = input('Stock Symbol:')


main()
