# 请求链接https://openapi.vmall.com/mcp/content/getPageInfoListAsync?pageId=257&lang=zh_CN&country=CN&portal=2
# 请求方式：GET
# 请求参数：pageId=257&lang=zh_CN&country=CN&portal=2

import requests
import ast

url = "https://openapi.vmall.com/mcp/content/getPageInfoListAsync"
params = {
    "pageId": 301,
    "lang": "zh_CN",
    "country": "CN",
    "portal": 1
}

headers = {
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Cookie': 'cps_id=78138; HWWAFSESID=a6e281991810eef8d25; HWWAFSESTIME=1699768939426; rnpersonalurlweb=https%3A%2F%2Fwww.vmall.com%2Fportal%2Fpersonal%2Findex.html%3FpageId%3D401001097; callAB=1; deviceid=ccfc84c9e1d57e442ee8d56efe686cb8; TID=ccfc84c9e1d57e442ee8d56efe686cb8; showAds=true; cartId=517992b19ba7479e9d384a763bd962a4; salePortal=1; rnpersonalurlwap=https%3A%2F%2Fm.vmall.com%2Fportal%2Fpersonal%2Findex.html%3FpageId%3D104001642; name=187****7065; nickname=V**********; isVpro=0; hasLogin=1699769930646; consumeYear=0; isGroupUser=false; ipaddressIdRN=6147%7C6148%7C6149; euid=8b3b0c855eeb5ee29790e83a1efb366cda16fd7ed27b4e55; isFirstLogin=0; aliToken=""; ageGroupFlag=0; optBanding=0; weChatInfo=false; ac_loNa=187****7065; ac_lel=""; ac_lmi=187****7065; ac_lus=1; ac_lgc=0; ac_ltp=0; ac_li=true; ac_cp=1500721829297|1500721912154|1500721969899|1599634375481; rush_info=70086200302227730_1699775967_SECD69950E5039122BF6AC90753448DB01CF23E6B8B428C697C81BD91E7B8073206; rush_ext=70086200302227730_1_0_1699775967_SEC7111287C511F156E5D9A5A9CBE90042B6802E1438CC58AE13018BA721F8C0447; uid=70086200302227730; user=18782817065; hasphone=1; displayName=V**********; recommendflag=0; grouptags=99140|94266|99183; CSRF-TOKEN=fbFVgLGtHvTIpsz5xnF6kaNsyofHFaAl88HJ; referer=https://www.vmall.com/order/nowConfirmcart; hasSigned=1; device_data=*2k94EVgM0MpDGmDWmETSjTT2MYNMhPUNZMkYAMUJdLU4DwG3X1T0jySz2xzyTm6ZYdJYbJNRMMOZW4DiTOclIcZAJMYctYyl30lj40hipO3wi3oxxumzy3l0MZNIIbZYZJZNUZdkgbMUAbZFYMMUYMLIUYOA4MyDmxtmjzkDjzljTuwST2rEjwziC9oTiywzDzijNbUgABElV0VQxRUAlM944Ug0YgQED4xmG1iD32LZIPMVIZNYQXTT2zGVWjjWjj22CGTSjyHTDWz13ZNZJMcMQOdlMZNVcNPRZOb1ZMVIUecMtZKEUNZDW15jn21WmhwGjUzTEGwG2yujEu12214DCkimzvyNJZObZYNMYbZZQVKMMRZNJbNYWl2DzxzjzjlAJccEQMMFFNNJ5zhwk422vlmulyyIlyyumpzz4gPdUad0YNY9RNNg0MeRUZY15Ybl5MJxJVbUUMRUTlwzmzlmDjhSmoyiTw0ETvtCSkwSz39nj30TzxYHF0ZlNMZgRkFZAdF1tNVYF0ZZcjkWmxh2DjwmmZdPIZMMccMYcNmDjTWTWTDjDUkjDTSmy2TDjDmqlQZMJMOMBJJZdIbOVlNNkpJPl9MbNVJJINZZUGk2mD5h2jxNGXvuyF0l2EDymFyySGuw2D4nGW4vHVNJJONNZJJOMeLJKJMaNMMNNYM4Tj44nj2imWjYEdIYJEzhl0wsCwymwxWZMOdPFJQMAb1cYSJcF52wz13uGp2MEhj9D3DhmN0RQ0ZEIlUFMZG2mmDkXQ==; sdevid=a60eb5a45071cab05b2ba6b4acacc339902f006b; rncategoryviewurl=https%3A%2F%2Fwww.vmall.com%2Fportal%2Fcategory%2Findex.html%3FpageId%3D103040874; cps_wi=',
    'Host': 'openapi.vmall.com',
    'Origin': 'https://www.vmall.com',
    'Referer': 'https://www.vmall.com/',
    'Sec-Ch-Ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
}

response = requests.get(url, params=params, headers=headers)
if response.status_code == 200:
    print("请求成功")
    pageInfos = response.json().get("pageInfos", [])
    cards = pageInfos[0].get("cards", [])
    for info in cards:
        try:
            category = ast.literal_eval(info.get("configInfo")).get("cardTitle")
            if category == "手机专区":
                # print(info.get("dataSourceList"))
                for dataSourceList in info.get("dataSourceList"):
                    dataInfos = dataSourceList.get("product").get("dataInfos")
                    productDict = {}
                    for dataInfo in dataInfos:
                        actionUrlWeb = dataInfo.get("actionUrlWeb")
                        prdName = dataInfo.get("prdName")
                        productDict[prdName] = actionUrlWeb
                        print(prdName, actionUrlWeb)
        except:
            continue
