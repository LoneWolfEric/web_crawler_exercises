import requests
from retrying import retry

url = 'http://zhjw.scu.edu.cn/loginAction.do'

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'Cookie':'JSESSIONID=dabJbxDzumHiegNr7vvow'
}

data = {
    'zjh': '2016141442100',
    'mm': '081318'
}

response = requests.post(url, data = data, headers = headers)

with open('jwc.html', 'w') as f:
    f.write(response.content.decode('gbk'))