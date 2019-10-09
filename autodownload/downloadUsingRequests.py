#from lxml import html
#import requests

#page = requests.get('https://www.coinbase.com/price')
#tree = html.fromstring(page.content)

#prices = tree.xpath('//h4[@class="Header__StyledHeader-sc-1q6y56a-0 hZxUBM TextElement__Spacer-sc-18l8wi5-0 hpeTzd"]/text()')
#print(prices[0])

#coinbase.com api: https://developers.coinbase.com/api/v2?python#authentication
import requests #pip install requests
print(float(requests.get("https://api.coinbase.com/v2/prices/BTC-USD/buy").json()["data"]["amount"])) #value for bitcoin.
