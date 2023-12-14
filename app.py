import time
import os
import cv2
import numpy as np
from tensorflow import keras
from PIL import Image
from flask import Flask, request, redirect, render_template
from keras.models import load_model

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

model_used = 'D:\\SEMESTER 7\\Praktikum Machine Learning\\New folder\\PRAKTIKUM\\PRAKTIKUM\\MODUL 6\\model\\model6.h5'

def predict_result(model, run_time, probs, img):
    idx_pred = probs.index(max(probs))
    labels = ['Paper', 'Rock', 'Scissors']
    return render_template('/result.html', labels=labels,
                            probs=probs, model=model, pred=idx_pred,
                            run_time=run_time, img=img)
@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route("/")
def index():
    return render_template('/index.html', )

@app.route('/predict', methods=['POST'])
def predict():
    model = load_model(model_used)

    file = request.files["file"]
    file.save(os.path.join('static', 'temp.jpg'))
    img = cv2.cvtColor(np.array(Image.open(file)), cv2.COLOR_BGR2RGB)
    img = np.expand_dims(cv2.resize(img, (224,224)).astype('float32') / 255, axis=0)
    
    start = time.time()

    pred = model.predict(img)[0]
    labels = (pred > 0.5).astype(int)

    runtimes = round(time.time()-start,4) 

    respon_model = [round(elem * 100, 2) for elem in pred] 
    
    return predict_result('CLASS', runtimes, respon_model, 'temp.jpg')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=2000)