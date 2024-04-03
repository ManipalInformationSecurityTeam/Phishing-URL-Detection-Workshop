from flask import Flask, request
import json
import pickle
import numpy as np
import tensorflow as tf

app = Flask(__name__)
    
@app.route('/', methods=['POST'])
def home():
    payload = request.get_json(force=True)
    model = tf.keras.models.load_model('model/model.h5')
    tokenizer = pickle.load(open('model/tokenizer.pkl', 'rb'))
    vectorizer = pickle.load(open('model/vectorizer.pkl', 'rb'))
    stemmer = pickle.load(open('model/stemmer.pkl', 'rb'))
    url = payload['url']
    tokens = tokenizer.tokenize(url)
    for token in tokens:
        token = stemmer.stem(token)
    url_tokenized = " ".join(tokens).strip()
    url_vectorized = vectorizer.transform([url_tokenized])
    url_prob = model.predict(url_vectorized.toarray())
    prediction = np.where(url_prob > 0.6, 'Bad URL', 'Good URL')
    return json.dumps({'prediction': str(prediction[0][0])})

if __name__=='__main__':
    app.run(debug=True)