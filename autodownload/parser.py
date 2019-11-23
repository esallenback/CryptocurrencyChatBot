import nltk
from nltk.tokenize import word_tokenize

# returns a tokenized input with all cryptos replaced by dummy variables,
# and a list for which cryptos each dummy variable corresponds to
def parse(input):
    file = open("cryptocurrencies.txt" , "r")
    cryptos = [item.strip() for item in file.readlines()]

    input = nltk.tokenize.word_tokenize(input)
    i = 0;
    crypto_list = []
    parsed_input = []
    for word in input:
        if word in cryptos:
            crypto_list.append(word.strip())
            word = 'crypto' + str(i)
            i = i+1
        parsed_input.append(word)

    parsedd = list2string(parsed_input)

    file.close()
    return [parsedd, crypto_list]


# takes in a input containing dummy crypto names and replaces with
# actual cryptos
def unparse(input, cryptos):
    output = ""
    if len(input)-1 > len(cryptos):
        return "off-topic"
    for i in range(len(input)-1):
        curInput = nltk.tokenize.word_tokenize(input[i+1])
        unparsed = []
        for word in curInput:
            if word == 'crypto0':
                word = cryptos[0].strip()
            elif word == 'crypto1':
                word = cryptos[1].strip()
            elif word == 'crypto2':
                word = cryptos[2].strip()
            unparsed.append(word)

        output += list2string(unparsed)

    return output


def list2string(list):
    output = ""
    for token in list:
        output = output + token + " "

    return output
