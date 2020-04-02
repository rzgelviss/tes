from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import urllib.request
from bs4 import BeautifulSoup as bs
import re
import os
import socket

# ****************************************************
base_url_part1 = 'https://www.bing.com/images/search?q='
base_url_part2 = '&qs=n&form=QBIR&sp=-1&pq=林&sc=8-1'  # base_url_part1以及base_url_part2都是固定不变的，无需更改
# search_query = '船'  # 检索的关键词，可自己输入你想检索的关键字
location_driver = 'D:\Ren\ggxz/chromedriver.exe'  # Chrome驱动程序在电脑中的位置


class Crawler:
    def __init__(self):
        self.url = base_url_part1 + search_query

    # 启动Chrome浏览器驱动
    def start_brower(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-infobars")
        # 启动Chrome浏览器
        driver = webdriver.Chrome(executable_path=location_driver, chrome_options=chrome_options)
        # 最大化窗口，因为每一次爬取只能看到视窗内的图片
        driver.maximize_window()
        # 浏览器打开爬取页面
        driver.get(self.url)
        return driver

    def downloadImg(self, driver):
        t = time.localtime(time.time())
        foldername = str(t.__getattribute__("tm_year")) + "-" + str(t.__getattribute__("tm_mon")) + "-" + \
                     str(t.__getattribute__("tm_mday"))  # 定义文件夹的名字
        picpath = 'E:/ImageDownload/%s/%s' % (foldername, search_query)  # 下载到的本地目录
        # 路径不存在时创建一个
        if not os.path.exists(picpath):
            os.makedirs(picpath)
        # 下载图片的本地路径 /home/LQ/ImageDownload/xxx

        # 记录下载过的图片地址，避免重复下载
        img_url_dic = {}
        x = 0
        # 当鼠标的位置小于最后的鼠标位置时,循环执行
        pos = 0
        socket.setdefaulttimeout(20)
        for i in range(10):  # 此处可自己设置爬取范围
            pos = i * 500  # 每次下滚500
            js = "document.documentElement.scrollTop=%d" % pos
            driver.execute_script(js)
            time.sleep(10)
            # 获取页面源码
            html_page = driver.page_source
            # 利用Beautifulsoup4创建soup对象并进行页面解析
            soup = bs(html_page, "html.parser")
            # print(soup)
            # print(type(soup))
            # 通过soup对象中的findAll函数图像信息提取
            imglist = re.findall(r'"murl":"(.*?)"', str(soup))
            print(imglist)
            print(len(imglist))
            # ??这段代码问题?
            for imgurl in imglist:
                print(imgurl)
                try:
                    print(x, end=' ')
                    if imgurl not in img_url_dic:
                        target = '{}/{}.jpg'.format(picpath, imgurl.split('/')[-1].split('.')[0])
                        # print ('Downloading image to location: ' + target + '\nurl=' + imgurl['src'])
                        img_url_dic[imgurl] = ''
                        try:
                            urllib.request.urlretrieve(imgurl, target)
                        except Exception as e:
                            print(e)
                            count = 1
                            while count <= 2:
                                try:
                                    urllib.request.urlretrieve(imgurl, target)
                                    break
                                except Exception as e:
                                    err_info = 'Reloading for %d time' % count if count == 1 else 'Reloading for %d times' % count
                                    print(err_info)
                                    count += 1
                            if count > 5:
                                print("downloading picture fialed!")

                        time.sleep(1.5)
                        x += 1
                except Exception as e:
                    print(e)
                    continue

    def run(self):
        print(
            '\t\t\t**************************************\n\t\t\t**\t\tWelcome to Use Spider\t\t**\n\t\t\t**************************************')
        driver = self.start_brower()
        self.downloadImg(driver)
        # driver.close()
        print("Download has finished.")


if __name__ == '__main__':
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context
    li = ['手拿保温杯', '手拿杯子', '手握杯子', '握杯子', '手拿杯子的图片', '手捧杯子', '手拿保温杯图片', '保温杯不离手图片']
    for i in li:
        search_query = i
        craw = Crawler()
        craw.run()
