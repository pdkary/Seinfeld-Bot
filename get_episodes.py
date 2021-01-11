from bs4 import BeautifulSoup, NavigableString
import requests
import re

def extract_quotes(a_str):
    contents = a_str.contents
    if contents is not None and len(contents)!=0:
        if type(contents[0]) == NavigableString:
            if "The" in contents[0].string:
                return contents[0].string
    else:
        return False

# website = requests.get('http://www.seinfeldscripts.com')
with open('seinfeld-scripts.html') as fp:
    soup = BeautifulSoup(fp,'html.parser')

links = []
for x in soup.find_all('a'):
    name = extract_quotes(x)
    if name:
        name = name.replace('\n','').replace(" ","").replace("(1)","").replace("(2)","2").replace('-','') + "\n"
        links.append(name)

with open('episodes.txt','w+') as fp:
    fp.writelines(links)