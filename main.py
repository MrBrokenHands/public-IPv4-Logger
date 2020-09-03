from requests import get

ip = get('https://api.ipify.org').text

f = open("ip.txt", "w")
f.write("{}".format(ip))
f.close()
#input()
