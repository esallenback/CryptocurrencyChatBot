# python3 test.py --test_data_file=./data/data.csv --run_dir=./runs/<MODEL_NAME> --checkpoint=clf-300

# -*- coding: utf-8 -*-
import os
import numpy as np
import pickle as pkl
import re
import nltk
import tensorflow as tf
from tensorflow.contrib import learn


def cryptoIdentifier(input):
    crypto_dict = dict({"bitcoin": "BTC",
                       "btc": "BTC",
                       "ethereum": "ETH",
                       "eth": "ETH",
                       "litecoin": "LTC",
                       "ltc": "LTC",
                       "dai": "DAI",
                       "eos": "EOS",
                       "stellar": "XLM",
                       "xlm": "XLM",
                       "bat": "BAT",
                       "ripple": "XRP",
                       "xrp": "XRP",
                       "chainlink": "LINK",
                       "link": "LINK",
                       "dash": "DASH",
                       "tezos": "XTZ",
                       "xtz": "XTZ",
                       "zcash": "ZEC",
                       "zec": "ZEC",
                       "ox": "ZRX",
                       "zrx": "ZRX",
                       "augur": "REP",
                       "rep": "REP"})
    input = nltk.tokenize.word_tokenize(input)

    for word in input:
        if word in crypto_dict:
            return word
    return None



def _clean_data(sent, sw, language='ch'):
    """ Remove special characters and stop words """
    if language == 'ch':
        sent = re.sub(r"[^\u4e00-\u9fa5A-z0-9！？，。]", " ", sent)
        sent = re.sub('！{2,}', '！', sent)
        sent = re.sub('？{2,}', '！', sent)
        sent = re.sub('。{2,}', '。', sent)
        sent = re.sub('，{2,}', '，', sent)
        sent = re.sub('\s{2,}', ' ', sent)
    if language == 'en':
        sent = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", sent)
        sent = re.sub(r"\'s", " \'s", sent)
        sent = re.sub(r"\'ve", " \'ve", sent)
        sent = re.sub(r"n\'t", " n\'t", sent)
        sent = re.sub(r"\'re", " \'re", sent)
        sent = re.sub(r"\'d", " \'d", sent)
        sent = re.sub(r"\'ll", " \'ll", sent)
        sent = re.sub(r",", " , ", sent)
        sent = re.sub(r"!", " ! ", sent)
        sent = re.sub(r"\(", " \( ", sent)
        sent = re.sub(r"\)", " \) ", sent)
        sent = re.sub(r"\?", " \? ", sent)
        sent = re.sub(r"\s{2,}", " ", sent)
    if sw is not None:
        sent = "".join([word for word in sent if word not in sw])

    return sent


def predict(input):
# if __name__ == "__main__":

    # Show warnings and errors only
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

    # File paths
    # tf.flags.DEFINE_string('test_data_file', "./data/test.csv", 'Test data file path')
    # tf.flags.DEFINE_string('run_dir', "blstm_model", 'Restore the model from this run')
    # tf.flags.DEFINE_string('checkpoint', "clf-300", 'Restore the graph from this checkpoint')

    # Test batch size
    # tf.flags.DEFINE_integer('batch_size', 1, 'Test batch size')
    # tf.flags.DEFINE_string('input', None, 'Input')

    # FLAGS = tf.app.flags.FLAGS
    # input = FLAGS.input
    run_dir = 'TextClassification/model'
    checkpoint = 'clf-900'

    # Restore parameters
    with open(os.path.join(run_dir, 'params.pkl'), 'rb') as f:
        params = pkl.load(f, encoding='bytes')

    # Restore vocabulary processor
    vocab_processor = learn.preprocessing.VocabularyProcessor.restore(os.path.join(run_dir, 'vocab'))

    # Restore graph
    graph = tf.Graph()
    with graph.as_default():
        sess = tf.Session()
        # Restore metagraph
        saver = tf.train.import_meta_graph('{}.meta'.format(os.path.join(run_dir, 'model', checkpoint)))
        # Restore weights
        saver.restore(sess, os.path.join(run_dir, 'model', checkpoint))

        # Get tensors
        input_x = graph.get_tensor_by_name('input_x:0')
        input_y = graph.get_tensor_by_name('input_y:0')
        predictions = graph.get_tensor_by_name('softmax/predictions:0')
        sequence_length = graph.get_tensor_by_name('sequence_length:0')
        batch_size = graph.get_tensor_by_name('batch_size:0')
        keep_prob = graph.get_tensor_by_name('keep_prob:0')
        accuracy = graph.get_tensor_by_name('accuracy/accuracy:0')


        # format input
        sent = input.strip().lower()
        sent = _clean_data(sent, None, 'en')
        formatted_inp = np.array(list(vocab_processor.transform([sent])))
        input_length = np.array(list(map(len, [sent.strip().split(' ')])))

        # print("INPUT: ", formatted_inp)
        # print("INPUT: ", sent)
        # print([sent.strip().split(' ')])

        feed_dict = {input_x: formatted_inp, input_y: [1], batch_size: 1, sequence_length: input_length, keep_prob: 1.0}
        # raw_pred, acc = sess.run([predictions, accuracy], feed_dict)
        # print(sess.run([predictions, accuracy], feed_dict)[0][0])
        raw_pred = sess.run([predictions, accuracy], feed_dict)[0][0]

        if (raw_pred == 0):
            pred = 'price'
        if (raw_pred == 1):
            pred = 'about'
        if (raw_pred == 2):
            pred = 'cryptointro'
        if (raw_pred == 3):
            pred = 'high'
        if (raw_pred == 4):
            pred = 'low'
        if (raw_pred == 5):
            pred = 'marketcap'
        if (raw_pred == 6):
            pred = 'volume'
        if (raw_pred == 7):
            pred = 'absolute'
        if (raw_pred == 8):
            pred = 'percent'
        if (raw_pred == 9):
            pred = 'close'
        if (raw_pred == 10):
            pred = 'opens'

        ret = [pred, cryptoIdentifier(input)]

        return ret

        # return pred
        # print("PREDICTION: ", pred)
