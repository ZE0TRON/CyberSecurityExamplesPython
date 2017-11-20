import urllib3

url1=""
url2=""
http = urllib3.PoolManager()
response = http.request("GET",url1)
print(response.data)
