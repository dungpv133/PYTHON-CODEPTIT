import re
xau = input()
hoa = len(re.findall(r'[A-Z]',xau))
thuong = len(re.findall(r'[a-z]',xau))
if(hoa > thuong):
    print(xau.upper())
else:
    print(xau.lower())