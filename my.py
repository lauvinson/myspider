"""
蠕虫
"""

from bs4 import BeautifulSoup
import utils.http
import mask.constants as mc

url = "http://zb.lubanjianye.com"
header = mc.common_user_agent
header["refresh"] = url
header["Host"] = url
cookies = "BD_UPN=12314753; BDUSS=EVLVlp3N1BYUGFnY2FYT3d1VHl0a08zNlU5clNXZ3h6UjBFa094aFJjekNZZ0JkSVFBQU" \
          "FBJCQAAAAAAAAAAAEAAAA8ZNcxbGF1dmluc29uAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" \
          "AAAAAAAAAAAAAAAAAAMLV2FzC1dhcN; BIDUPSID=233FB42423D4114C16DD521412344C6B; PSTM=1559646786; _" \
          "_cfduid=dfd0d3a7d543d800e9cf20ddb9d0459771560991332; BAIDUID=8D8D112547DF86F4AE6884219807337" \
          "7:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BD_CK_SAM=1; PSINO=1; ispeed=1; COOKIE_SESSION" \
          "=316_0_7_2_4_8_1_1_4_3_3_1_227172_0_0_0_1561338269_0_1561339160%7C9%230_0_1561339160%7C1; delPe" \
          "r=1; H_PS_645EC=6415j2DcN1b3Ov7YjxA%2F6zX3VR%2B4ZvAYoHMBeYY%2BhcGKzDl%2Fm8gAYddpkN8; ispeed_ls" \
          "m=5; BD_HOME=1; H_PS_PSSID=26525_1455_21123_29135_29238_28518_29099_29131_29369_28833_29220; s" \
          "ug=0; sugstore=0; ORIGIN=0; bdime=0"
cookie_dict = {i.split("=")[0]: i.split("=")[-1] for i in cookies.split("; ")}
r = utils.http.get(url, headers=mc.common_user_agent, cookies=cookie_dict)

# 创建 Beautiful Soup 对象
html = BeautifulSoup(r.content.decode(), "lxml")

# 格式化输出 soup 对象的内容
print(html.prettify)
