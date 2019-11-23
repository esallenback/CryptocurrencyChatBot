from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named Charlie
cryptobot = ChatBot(
    'CryptoBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///chatterbotstorage.sqlite3',
    read_only = True
)

trainer = ListTrainer(cryptobot)

file = open("trainingdata.txt" , "r")
data = [item.strip() for item in file.readlines()]

i = 0
while i < len(data):
    trainer.train([
        data[i],
        data[i+1]
    ])
    i += 3

file.close()
