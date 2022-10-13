from bs4 import BeautifulSoup as bs
import re
import requests
import json
request = requests.get("https://www.ascii-code.com/")
soup = bs(request.text, "html.parser")
meaningP = soup.find_all("tr")
meaningP
Meaning  = ""
data = {}
meaningP.pop(0)
meaningP.pop(32)
meaningP.pop(128)
data = [str(element) for element in meaningP]
i=0
dictionary = {}
for x in data:
  line  = str(x)
  length = len(line)
  first = line.index('<td>', 0, length)
  second = line.index('<td>', first+1, length)
  third = line.index('<td>', second+1,length)
  forth = line.index('<td>', third+1, length)
  fivety = line.index('<td>', forth+1, length)
  sixty = line.index('<td>', fivety+1, length)
  formline2 = line[sixty+4:length]
  tdclose = formline2.index('</td>')
  formline = line[fivety+4:fivety+12]
  formline2 = formline2[0:tdclose]
  dictionary[formline] = formline2.replace(" ", "")
  i = i + 1
print(dictionary)