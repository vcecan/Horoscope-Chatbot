import random
import json
import pickle
import numpy as np
from textblob import TextBlob
import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model

import re 


from request import horoscopes
from seq2seq import seqresponse




lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))
model = load_model('chatbot_model.h5')
model_seq = load_model('model_attention.h5')



def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(str(sentence))
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def spelling_correction(sentence):
    clear_text = re.sub('[^a-zA-Z]', ' ', str(sentence))
    correct_text=TextBlob(clear_text)
    correct_text=correct_text.correct()
    print(correct_text)
    return correct_text
#spelling
def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words)
    for w in sentence_words:
        for i,word in enumerate(words):
            if word == w:
                bag[i] = 1

    return np.array(bag)
def horoscope_request(sentence):
    sentence_words = clean_up_sentence(sentence)
    for w in sentence_words:
        if w == "libra":
            return horoscopes[6]
        if w == "scorpio":
            return horoscopes[7]
        if w == "sagittarius":
            return horoscopes[8]
        if w == "capricorn":
            return horoscopes[9]
        if w == "aquarius":
            return horoscopes[10]
        if w == "pisces":
            return horoscopes[11]
        if w == "aries":
            return horoscopes[0]
        if w == "taurus":
            return horoscopes[1]
        if w == "gemini":
            return horoscopes[2]
        if w == "cancer":
            return horoscopes[3]
        if w == "lion":
            return horoscopes[4]
        if w == "virgo":
            return horoscopes[5]

def predict_class(sentence):
    global seq_flag
    seq_flag=0
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    print (f'res{res}')
    ERROR_THRESHOLD =0.85
    results = [[i,r] for i,r in enumerate(res) if r > ERROR_THRESHOLD]
    if results==[]:
         seq_flag=1



    print(f'results unu: {results}')
    results.sort(key=lambda x: x[1],reverse = True)
    print(f'results  {results}')
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability' : str(r[1])})
    return return_list


def get_response(intents_list, intents_json,message):
    #global result
    global seq_flag
    if seq_flag==0:
        tag = intents_list[0]['intent']
        list_of_intents = intents_json['intents']
        for i in list_of_intents:
            if i['tag'] == tag:
                if i['tag'] =='greetings':
                    result = random.choice(i['responses']) + ", how can i help you?"
                elif i['tag'] == 'signs':
                     result=horoscope_request(message)
                elif i['tag'] =='thanks':
                    result = random.choice(i['responses']) + ", what can i do else?"
                elif i['tag'] =='whatsup':
                    result = random.choice(i['responses']) + ", what about you?"
                else:
                    result = random.choice(i['responses'])
                break
    else:
        result=seqresponse(str(message))
    return result

def get_message_response(message):
#while True:
    #message= input("").lower()
    ints = predict_class(message)
    res = get_response(ints, intents,message)
    print (res)
    return res

#message_discord= input("").lower()
#get_message_response((message_discord))
#print (res)