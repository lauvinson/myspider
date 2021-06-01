"""
蠕虫
"""
import json

import mask.constants as mc
import utils.http

host = "https://www.mihuashi.com"
header = mc.common_user_agent
# header["authority"] = 'www.mihuashi.com'
# header["method"] = 'GET'
# header["scheme"] = 'https'
header[
    "accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
header["accept-language"] = "zh-CN,zh;q=0.9"
header["accept-encoding"] = "gzip, deflate, br"
header["sec-ch-ua"] = "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"90\", \"Google Chrome\";v=\"90\""
header["sec-ch-ua-mobile"] = "?0"
header["sec-fetch-dest"] = "document"
header["sec-fetch-mode"] = "navigate"
header["sec-fetch-site"] = "none"
header["sec-fetch-user"] = "?1"
cookies = "__auc=812371f8179c5d5d1efde79b15f; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22179c5d5dd121f0-00df5a99c33ad3-2363163-2073600-179c5d5dd138ba%22%2C%22%24device_id%22%3A%22179c5d5dd121f0-00df5a99c33ad3-2363163-2073600-179c5d5dd138ba%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _ga=GA1.2.69100424.1622521799; _gid=GA1.2.640807596.1622521799; __asc=674b3592179c62de9371b6a9e73; _gat=1"
cookie_dict = {i.split("=")[0]: i.split("=")[-1] for i in cookies.split("; ")}

links = []
for i in range(1000):
    try:
        path = '/api/v1/artworks/search?page=' + str(i + 1) + '&type=recent'
        header["path"] = path
        url = host + path
        r = utils.http.get(url, headers=header, cookies=cookie_dict)
        if r.status_code == 200:
            r_dic = json.loads(r.text)
            for e in r_dic["artworks"]:
                links.append(e["url"])
    except:
        continue

try:
    filename = open('C:\\Users\\Administrator\\Downloads', 'w')  # dict转txt
    for i in links:
        filename.write(i + '\n')

    filename.close()
except:
    pass
