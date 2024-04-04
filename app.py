import streamlit as st
import nltk
from nltk.corpus import stopwords
import string
import pickle
from nltk.stem.porter import PorterStemmer

nltk.download("punkt")
nltk.download("stopwords")

ps = PorterStemmer()

tfidf = pickle.load(open("vectorizer.pkl", "rb"))
voting = pickle.load(open("voting.pkl", "rb"))

def transform(text):
    L = []
    for i in text.split():
        if i != "Subject:":
            L.append(i)
    text =  " ".join(L)

    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words("english") and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))
    
    return " ".join(y)

st.title("SpamGuard: Ultimate Email/SMS Spam Classifier")

input_text = st.text_area("Enter Email/SMS: ")

if st.button("Predict"):
    # 1. Transform text
    transformed_text = transform(input_text)
    # 2. Vectorize
    X = tfidf.transform([transformed_text]).toarray()
    # 3. Predict
    prediction = voting.predict(X)
    # 4. Display
    if prediction == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")