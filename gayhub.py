import requests
from retrying import retry

url = 'https://github.com/settings/profile'

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'Cookie':'_ga=GA1.2.1082273421.1520517213; _octo=GH1.1.1067171400.1520517213; tz=Asia%2FShanghai; _gat=1; user_session=ZxlQPJiOC9IVz2H8GlCHuhxN_IODAmEbldDSQ5-W4ZBs6VPl; __Host-user_session_same_site=ZxlQPJiOC9IVz2H8GlCHuhxN_IODAmEbldDSQ5-W4ZBs6VPl; logged_in=yes; dotcom_user=LoneWolfEric; _gh_sess=SHlWaitJRHk0MTk4RS9JZUVFRXRrUlZPRStBOTVuRDg4UFR2eDB2NkdTU0ZIYkJma3NxdWpuM2ozUnhkKytZdktaTmlBcktQcEFPRlJNZmNHRlBhalZEaXkxYlhXaHcxd25BbWxGOWtWb0ZkN3liZ2ExME4xRXFuOENlSUtJc0hiekpsZG53SlQ3Z3dUSFlKdnZ3VXI0emlmR2grOVZ5dDliZFNjMWRab0xTY2xYOVY3QXJBZjVpS28wTVNBdDJwelo1cS96UlBBWVRsYVVqcVRvU1BOQ2VweXd4SVhTT3Bodk91R1hFMVdJMy9LblE0amF6MWJlSk9wU2tNYVdJVUtyTnVOV2pRMGNVZnk4K3k1T0F3MW8zNUlpMTRrVXFkQnBEdGNhRG1hYmtySmxVUU05bG1vWm1JZGpSTElqYlotLTBNOWNMWFpHcEpMOUxqUmVjL21xb3c9PQ%3D%3D--ab725e42d4773bfbf3d9d318d553939a4b64a719'
}

response = requests.get(url, headers = headers, timeout = 20)

with open('gayhub.html', 'w') as f:
    f.write(response.content.decode())