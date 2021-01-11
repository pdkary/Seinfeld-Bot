from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


chatbot = ChatBot(
    'Jerry',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3')
    
# trainer = ChatterBotCorpusTrainer(chatbot)
# trainer.train(
#     "chatterbot.corpus.english.greetings",
#     "chatterbot.corpus.english.conversations",
#     "./scripts/corpus/"
# )

response = chatbot.get_response('Where is my car?')

for i in range(50):
    if i%2==0:
        print("Chatbot1: " + str(response))
    else:
        print("Chatbot2: " + str(response))
    response = chatbot.get_response(response)