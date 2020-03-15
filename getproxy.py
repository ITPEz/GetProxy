import requests

print("This Script To Get Custom Proxy")
print("Code : NOOBKP")
print("Latest Update : 15/3/2020\n")
type = str(input("Type : socks4 / socks5 / http / https  : "))
cty = str(input("Country : TW / CN / US / all : "))
anon = str(input("Anonymity : anonymous / elite / all : "))
to = str(input("Timeout : "))
sl = str(input("SSL Mode : yes / no / all : "))
file = str(input("File Name : "))
rsp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype='+str(type)+'&country='+str(cty)+'&anonymity='+str(anon)+'&ssl='+str(sl)+'&timeout='+str(to))
with open(str(file),'wb') as fp:
	fp.write(rsp.content)
	print("Save Proxy Success!")