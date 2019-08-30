import json
import requests

# url = "http://httpbin.org/post"
url = 'http://192.168.1.117:9002/'
data = {'username': 'zhangsan', 'password': 'zhangsanpw'}
data = json.dumps(data)
print(type(data))
r = requests.post(url, data=data)
# r = requests.get(url)
print(r.text)


# def http_post():
#     url = "http://152.1.12.11:8080/web"
#     postdata = dict(d=2, p=10)
#     post = []
#     post.append(postdata)
#     req = urllib2.Request(url, json.dumps(post)) #需要是json格式的参数
#     req.add_header('Content-Type', 'application/json') #要非常注意这行代码的写法
#     response = urllib2.urlopen(req)
#     result = json.loads(response.read())
#     print(result)