import urllib.request
import urllib.parse
import json

content = str(input("what do you want to translate:"))

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

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

response = urllib.request.urlopen(url, data)

html = response.read().decode('utf-8')

target = json.loads(html)

result = target['translateResult'][0][0]['tgt']

print(result)