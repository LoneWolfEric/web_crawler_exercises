# -*- coding: utf-8 -*-
import urllib.request

response = urllib.request.urlopen("http://placekitten.com/g/300/500")

cat_img = response.read()

with open('cat_img.jpg', 'wb') as f:
    f.write(cat_img)
