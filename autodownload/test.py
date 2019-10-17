import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import sys
import requests


def find_cur_crypto(words):
    cur_cryptos = []
    file = open("cryptocurrencies.txt" , "r")

    # creates list of all cryptos from cryptocurrencies.txt
    cryptos = [item.strip() for item in file.readlines()]

    # assigns cur_cryptos to any crypto found in cryptos
    for word in words:
        word = word.lower()
        if word in cryptos:
            cur_cryptos.append(word)

    if len(cur_cryptos) == 0:
        cur_cryptos.append("null")

    # returns list of all cryptos mentioned in the input
    return cur_cryptos;

def find_question(words):
    question = ""


    # creates list of all 'price question' indicators from price_words.txt
    file = open("price_words.txt" , "r")
    price_words = [item.strip() for item in file.readlines()]

    # creates list of all 'compare question' indicators from compare_words.txt
    file = open("compare_words.txt", "r")
    compare_words = [item.strip() for item in file.readlines()]

    # assigns question to 'price' if a price indicator is found
    for word in words:
        if word in price_words:
            question = "price"

    # 'compare' question takes precedence over 'price question'
    for word in words:
        if word in compare_words:
            question = "compare"

    return question;


if __name__ == '__main__':
    while True:
        # takes in input from command line
        query = input("> ")
        if query == "q":
            break;

        # tokenizes input sentence
        words = nltk.tokenize.word_tokenize(query)
        stopWords = set(nltk.corpus.stopwords.words("english"))
        for word in words:
            if word in stopWords:
                words.remove(word)

        cur_cryptos = find_cur_crypto(words)
        question = find_question(words)

        if len(cur_cryptos) <= 2:
            # determines default question
            if not question:
                if cur_cryptos[0] != "null":
                    question = "about"
                else:
                    question = "off topic"

            # print("~ will call '" +  question  + "' function on '", end = '')
            # print(cur_cryptos, end = '')
            # print("' crypto ~\n")
            if cur_cryptos[0] == "bitcoin" and question == "price":
                print("Current price of bitcoin: " + str(float(requests.get("https://api.coinbase.com/v2/prices/BTC-USD/buy").json()["data"]["amount"])))
            if cur_cryptos[0] == "ripple" and question == "price":
                print("Current price of ripple: " + str(float(requests.get("https://api.coinbase.com/v2/prices/XRP-USD/buy").json()["data"]["amount"])))
        else:
            print("I don't have the capacity to deal with more than 2 cryptos right now")
