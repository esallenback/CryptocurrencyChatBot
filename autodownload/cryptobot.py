from chatterbot import ChatBot
import nltk
from nltk.tokenize import word_tokenize

# Create a new chat bot named Charlie
cryptobot = ChatBot(
    'CryptoBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///chatterbotstorage.sqlite3',
    read_only = True
)


def respond(input):
    response = cryptobot.get_response(input)
    return nltk.tokenize.word_tokenize(str(response))
