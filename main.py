import speech_recognition as sr 
# from flask import Flask, render_template, jsonify, request

# import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
# from tqdm.notebook import tqdm
# app = Flask(__name__)
r = sr.Recognizer()
with sr.AudioFile('male.wav') as source:
     audio_text = r.listen(source)
     try:
         text_output = r.recognize_google(audio_text)
         print("Text converted from audio:\n")
         print(text_output)
         print("Finished!!")
     except:
            print("Couldn't process the audio input.")
text_output = "I am happy"
# tokens = nltk.word_tokenize(text_output)
# tagged = nltk.pos_tag(tokens)
# entities = nltk.chunk.ne_chunk(tagged)

sia = SentimentIntensityAnalyzer()

score = sia.polarity_scores(text_output)
print(score)

     