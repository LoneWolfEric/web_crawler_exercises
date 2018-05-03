import urllib.request

url = 'http://www.baidu.com'

req = urllib.request.Request(url)

response = urllib.request.urlopen(req)

html = response.read().decode('utf-8')

print(html)