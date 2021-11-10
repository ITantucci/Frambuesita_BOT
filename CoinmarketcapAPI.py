from requests import Request, Session
import json
import pprint
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

parameters = {
    'slug': "bitcoin,ethereum,smooth-love-potion,shiba-inu,cardano,chainlink,dogecoin,plantvsundead,cosmos,binance-coin,xrp",
    'convert': 'USD'
}
headers = {
    'Accepts': 'aplication/json',
    'X-CMC_PRO_API_KEY': 'API'

}

session = Session()
session.headers.update(headers)

def Get_Response():
    response = session.get(url, params=parameters)
    return response

def Set_BTC_Value(): 
     BTCValue = json.loads(Get_Response().text)["data"]['1']['quote']['USD']['price']
     return BTCValue

def Set_ETH_Value():
     ETHValue = json.loads(Get_Response().text)["data"]['1027']['quote']['USD']['price']
     return ETHValue

def Set_PVU_Value():
     PVUValue = json.loads(Get_Response().text)["data"]['11130']['quote']['USD']['price']
     return PVUValue

def Set_LINK_Value():
     LINKValue = json.loads(Get_Response().text)["data"]['1975']['quote']['USD']['price']
     return LINKValue

def Set_ADA_Value():
     ADAValue = json.loads(Get_Response().text)["data"]['2010']['quote']['USD']['price']
     return ADAValue

def Set_SLP_Value():
     SLPValue = json.loads(Get_Response().text)["data"]['5824']['quote']['USD']['price']
     return SLPValue

def Set_SHIB_Value():
     SHIBValue = json.loads(Get_Response().text)["data"]['5994']['quote']['USD']['price']
     return SHIBValue

def Set_DOGE_Value():
     DOGEValue =  json.loads(Get_Response().text)["data"]['74']['quote']['USD']['price']
     return DOGEValue

def Set_ATOM_Value():
     ATOMValue =  json.loads(Get_Response().text)["data"]['3794']['quote']['USD']['price']
     return ATOMValue

def Set_BNB_Value():
     BNBValue = json.loads(Get_Response().text)["data"]['1839']['quote']['USD']['price']
     return BNBValue

def Set_XRP_Value():
     XRPValue = json.loads(Get_Response().text)["data"]['52']['quote']['USD']['price']
     return XRPValue



def Set_BTC_1hr():
    BTCPercentlast1hr = json.loads(Get_Response().text)["data"]['1']['quote']['USD']['percent_change_1h']
    return BTCPercentlast1hr

def Set_ETH_1hr():
    ETHPercentlast1hr = json.loads(Get_Response().text)["data"]['1027']['quote']['USD']['percent_change_1h']
    return ETHPercentlast1hr

def Set_PVU_1hr():
    PVUPercentlast1hr = json.loads(Get_Response().text)["data"]['11130']['quote']['USD']['percent_change_1h']
    return PVUPercentlast1hr

def Set_LINK_1hr():
    LINKPercentlast1hr = json.loads(Get_Response().text)["data"]['1975']['quote']['USD']['percent_change_1h']
    return LINKPercentlast1hr

def Set_ADA_1hr():
    ADAPercentlast1hr = json.loads(Get_Response().text)["data"]['2010']['quote']['USD']['percent_change_1h']
    return ADAPercentlast1hr

def Set_SLP_1hr():
    SLPPercentlast1hr = json.loads(Get_Response().text)["data"]['5824']['quote']['USD']['percent_change_1h']
    return SLPPercentlast1hr

def Set_SHIB_1hr():
    SHIBPercentlast1hr = json.loads(Get_Response().text)["data"]['5994']['quote']['USD']['percent_change_1h']
    return SHIBPercentlast1hr

def Set_DOGE_1hr():
    DOGEPercentlast1hr = json.loads(Get_Response().text)["data"]['74']['quote']['USD']['percent_change_1h']
    return DOGEPercentlast1hr

def Set_ATOM_1hr():
    ATOMPercentlast1hr = json.loads(Get_Response().text)["data"]['3794']['quote']['USD']['percent_change_1h']
    return ATOMPercentlast1hr

def Set_BNB_1hr():
    BNBPercentlast1hr = json.loads(Get_Response().text)["data"]['1839']['quote']['USD']['percent_change_1h']
    return BNBPercentlast1hr

def Set_XRP_1hr():
    XRPPercentlast1hr = json.loads(Get_Response().text)["data"]['52']['quote']['USD']['percent_change_1h']
    return XRPPercentlast1hr




def Set_BTC_24hr():
    BTCPercentlast24hr = json.loads(Get_Response().text)["data"]['1']['quote']['USD']['percent_change_24h']
    return BTCPercentlast24hr

def Set_ETH_24hr():
    ETHPercentlast24hr = json.loads(Get_Response().text)["data"]['1027']['quote']['USD']['percent_change_24h']
    return ETHPercentlast24hr

def Set_PVU_24hr():
    PVUPercentlast24hr = json.loads(Get_Response().text)["data"]['11130']['quote']['USD']['percent_change_24h']
    return PVUPercentlast24hr

def Set_LINK_24hr():
    LINKPercentlast24hr = json.loads(Get_Response().text)["data"]['1975']['quote']['USD']['percent_change_24h']
    return LINKPercentlast24hr  

def Set_ADA_24hr():
    ADAPercentlast24hr = json.loads(Get_Response().text)["data"]['2010']['quote']['USD']['percent_change_24h']
    return ADAPercentlast24hr

def Set_SLP_24hr():
    SLPPercentlast24hr = json.loads(Get_Response().text)["data"]['5824']['quote']['USD']['percent_change_24h']
    return SLPPercentlast24hr

def Set_SHIB_24hr():
    SHIBPercentlast24hr = json.loads(Get_Response().text)["data"]['5994']['quote']['USD']['percent_change_24h']
    return SHIBPercentlast24hr

def Set_DOGE_24hr():
    DOGEPercentlast24hr = json.loads(Get_Response().text)["data"]['74']['quote']['USD']['percent_change_24h']
    return DOGEPercentlast24hr

def Set_ATOM_24hr():
    ATOMPercentlast24hr = json.loads(Get_Response().text)["data"]['3794']['quote']['USD']['percent_change_24h']
    return ATOMPercentlast24hr

def Set_BNB_24hr():
    BNBPercentlast24hr = json.loads(Get_Response().text)["data"]['1839']['quote']['USD']['percent_change_24h']
    return BNBPercentlast24hr

def Set_XRP_24hr():
    XRPPercentlast24hr = json.loads(Get_Response().text)["data"]['52']['quote']['USD']['percent_change_24h']
    return XRPPercentlast24hr




def MioBTC():
    return (Set_BTC_Value() * )

def MioETH():
    return (Set_ETH_Value() * )

def MioPVU():
    return (Set_PVU_Value() * )

def MioLINK():
    return (Set_LINK_Value() * )

def MioADA():
    return (Set_ADA_Value() * )

def MioSLP():
    return (Set_SLP_Value() * )

def MioSHIB():
    return (Set_SHIB_Value() * )

def MioDOGE():
    return (Set_DOGE_Value() * )

def MioATOM():
    return (Set_ATOM_Value() * )

def MioBNB():
    return (Set_BNB_Value() * ) 

def MioXRP():

    return (Set_XRP_Value() * )

def Total():
    Total =(MioBTC() + MioETH() + MioPVU() + MioLINK() + MioADA() + MioSLP() + MioSHIB() + MioDOGE() + MioATOM() + MioBNB() + MioXRP())
    return Total


#pprint.pprint(response.json())
