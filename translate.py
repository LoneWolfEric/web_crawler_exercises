import urllib.request
import urllib.parse
import json
import time

content = str(input("what do you want to translate:"))

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

# 修改user-agent来模仿人访问网页
head = {}

head['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'



# 填写request的form data，向服务器发起请求
data = {}

data['i'] = content
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '1525242671911'
data['sign'] = 'b0e57fd968985afa7a38f539f20337c8'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CLICKBUTTION'
data['typoResult'] = 'false'

data = urllib.parse.urlencode(data).encode('utf-8')

req = urllib.request.Request(url, data, head)

response = urllib.request.urlopen(req)

html = response.read()

target = json.loads(html)

result = target['translateResult'][0][0]['tgt']

print(result)