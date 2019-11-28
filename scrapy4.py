import requests
import os
from lxml import etree
from threading import *
import time
import requests
from lxml import etree
import sys
import json
import warnings

warnings.filterwarnings('ignore')
import re
# 请求头设置
headers = {
    "User-Agentv": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
    "Referer": "https://cn.bing.com/"
}
url = 'https://cn.bing.com/images/async?q={}&first={}&count=35&relp=35&cw=1129&ch=597&scenario=ImageBasicHover&datsrc=N_I&layout=RowBased_Landscape&mmasync=1&dgState=x*823_y*1573_h*168_c*3_i*36_r*9&IG=DA370CC831F54FEEBB57ADBEA83F81A2&SFX=2&iid=images.5644'

# /images/async?q=%e8%88%b9&first=106&count=35&relp=35&cw=1129&ch=597&scenario=ImageBasicHover&datsrc=N_I&layout=RowBased_Landscape&mmasync=1&dgState=x*0_y*0_h*0_c*4_i*106_r*26
# /images/async?q=%e8%88%b9&first=148&count=35&relp=35&cw=1129&ch=597&scenario=ImageBasicHover&datsrc=N_I&layout=RowBased_Landscape&mmasync=1&dgState=x*762_y*1528_h*181_c*3_i*141_r*35
# /images/async?q=%e8%88%b9&first=187&count=35&relp=35&cw=1129&ch=597&scenario=ImageBasicHover&datsrc=N_I&layout=RowBased_Landscape&mmasync=1&dgState=x*291_y*1576_h*186_c*1_i*176_r*44

i = 0
lis = ['船', '货船', '沙船', '河货船', '河沙船', '河船']
for j in lis:
    for k in range(10):

        num = k * 35 + 36
        # print(type(num))
        # print(num)
        url_ = url.format(j, num)
        print(url_)
        response = requests.get(url_, headers=headers).text
        # print(response)
        # print(re.findall(r'&quot;murl&quot;:&quot;(.*?)&quot', response))

        html = etree.HTML(response)
        # print(html)
        # // *[ @ id = "mmComponent_images_1"] / ul[1]
        ul = html.xpath('//*[@id="mmComponent_images_5644_2_1"]/ul')
        print(ul)
        top = 'https://cn.bing.com/'
        for li in ul:
            li = li.xpath('./li')
            # print(li)
            for img_url in li:
                # print(img)
                try:
                    img_ = img_url.xpath('./div/div/a/@m')[0]
                    # print(json.loads(img_))
                    # print(type(json.loads(img_)))
                    img_1 = json.loads(img_)
                    # print(img_1)
                    img_2 = img_1['murl']
                    print(img_2)
                    try:
                        img = requests.get(img_2, timeout=5, verify=False, stream=True).raw.read()

                        # print(img)
                        with open('./xm1/' + img_2.split('/')[-1], 'wb') as file:
                            file.write(img)
                        i += 1
                        print(i)
                    except:
                        print('time out')
                except:
                    print('list index out of range')
        k += 1


# https://cn.bing.com/images/async?q=%e8%88%b9&first=37&count=35&relp=35&scenario=ImageBasicHover&datsrc=N_I&layout=RowBased_Landscape&mmasync=1&dgState=x*798_y*1567_h*168_c*3_i*36_r*9&IG=E6DD404A60374DD3A99D9DCED05C1C97&SFX=2&iid=images.5646
# https://cn.bing.com/images/async?q=%e8%88%b9&first=72&count=35&relp=35&scenario=ImageBasicHover&datsrc=N_I&layout=RowBased_Landscape&mmasync=1&dgState=x*0_y*0_h*0_c*4_i*71_r*17&IG=E6DD404A60374DD3A99D9DCED05C1C97&SFX=3&iid=images.5646
# https://cn.bing.com/images/async?q=%e8%88%b9&first=107&count=35&relp=35&scenario=ImageBasicHover&datsrc=N_I&layout=RowBased_Landscape&mmasync=1&dgState=x*792_y*1599_h*189_c*3_i*106_r*26&IG=E6DD404A60374DD3A99D9DCED05C1C97&SFX=4&iid=images.5646
