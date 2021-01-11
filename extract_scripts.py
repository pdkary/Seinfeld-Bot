from bs4 import BeautifulSoup
import re
import os

LINE_STARTING_REGEX = "^[A-Za-z]{3,10}:"
bad_chars = ["\\","\n","\t","-","%","\"","\'",":",";","&","$","#","@","[","]","{","}","(",")","             ","        ","*","^","+",",",'`',"!","?"]
call_and_response_dict = {}

def sanitize(a_str):
    for c in bad_chars:
        a_str = a_str.replace(c,"")
    return str(a_str)
    
def extract_to_dict(filename):
    with open('scripts/html/'+filename+'.html','r+') as fp:
        soup = BeautifulSoup(fp,'html.parser')
        contents = soup.find(id="content")
        peas = [x.text for x in contents.find_all('p')]
    
    started = False
    script_lines = []
    tmp = []
    for x in peas:
        searched = re.search(LINE_STARTING_REGEX,x)
        if searched is not None:
            started=True
            tmp_str = " ".join(tmp)
            script_lines.append(tmp_str)
            tmp = []
        if started:
            tmp.append(x)

    with open('scripts/text/'+filename+'.txt','w+') as fp:
        for i,x in enumerate(script_lines):
            if i != len(script_lines)-1 and i != 0:
                call = x
                caller = re.search(LINE_STARTING_REGEX,call).group()[:-1].upper()
                new_start = re.search(LINE_STARTING_REGEX,call).span()[1]
                new_call = "- - " + "\"" + sanitize(call[new_start:]) + "\"" + "\n"

                response = script_lines[i+1]
                respondant = re.search(LINE_STARTING_REGEX,response).group()[:-1].upper()
                new_start = re.search(LINE_STARTING_REGEX,response).span()[1]
                new_response = "  - " + "\"" + sanitize(response[new_start:]) + "\"" + "\n"

                if respondant not in call_and_response_dict.keys():
                    call_and_response_dict[respondant] = []

                call_and_response_dict[respondant].append(new_call)
                call_and_response_dict[respondant].append(new_response)
    
            
with open('episodes.txt','r') as fp:
    episodes = [x.strip() for x in fp.readlines()]

if __name__ == "__main__":
    for ep in episodes:
        try:
            extract_to_dict(ep)
        except FileNotFoundError:
            continue

    crkeys = call_and_response_dict.keys()
    respondants = [] 
    for i in crkeys: 
        if i not in respondants: 
            respondants.append(i) 

    for respondant in respondants:
        with open("./scripts/corpus/"+respondant+".yml","a+") as corpus:
            corpus.write("categories:\n- english\n- greetings\nconversations:\n")

            for x in call_and_response_dict[respondant]:
                corpus.write(x)