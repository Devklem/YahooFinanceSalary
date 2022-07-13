from pandas import read_html as rh
import requests

def YahooCompensationData(tickD):
  rHTML = requests.get('https://finance.yahoo.com/quote/'+tickD+'/profile', headers = {'User-Agent':'Mozilla/5.0'})
  compDF = pd.read_html(rHTML.content)[0]
  compDF['Ticker'] = tickD
  return compDF
