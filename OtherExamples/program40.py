import requests
from bs4 import BeautifulSoup
url="http://www.google.com"
response = requests.get(url)
Text = response.text
soup = BeautifulSoup(Text,"html-parser")
links = [a.attrs.get("href") for a in soup.select("a[href]")]
print(links)
