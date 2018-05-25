import requests

url = 'http://www.baidu.com'

response = requests.get(url, timeout = 400)

response.encoding = 'utf-8'

print('response.request.url', response.request.url)
print('response.url', response.url)
print('response.request.headers', response.request.headers)
print('response.headers', response.headers)
