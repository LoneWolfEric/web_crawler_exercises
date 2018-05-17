import re

test = re.search(r'[a-z]', 'abc')

print(test)

ip = re.search(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])', '188.123.2.1')

print(ip)

sub = re.search(r'(abc)\1\1', 'abcabcabcdagregbr')

print(sub)

a = re.findall(r'(abc)\1\1', 'abcabcabcdagregbr')

print(a)