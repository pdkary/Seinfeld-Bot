from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

all_episodes = []

with open("episodes.txt","r") as fp:
    episodes = [x.strip() for x in fp.readlines()]

for ep in episodes:
    try:
        with open("scripts/text/"+ep+".txt",'r') as fp:
            all_episodes += [x.strip() for x in fp.readlines()]
    except FileNotFoundError:
        continue

chatbot = ChatBot(
    'Jerry',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'
    ],
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3')
    
trainer = ListTrainer(chatbot)

trainer.train(all_episodes)

response = chatbot.get_response('Hello Jerry')
for i in range(50):
    print(response)
    response = chatbot.get_response(str(response))