import os
import tensorflow as tf
from flask import Flask, request, render_template, jsonify
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np

app = Flask(__name__)
app.config['MODEL_PATH'] = os.path.join('static/model.h5')
app.config['UPLOAD_FOLDER'] = os.path.join('static/images')

model = load_model(app.config['MODEL_PATH'])
graph = tf.get_default_graph()
                                        
@app.route('/', methods=['GET', 'POST'])
def upload_and_predict():
    if request.method == 'POST':
        file = request.files['file']
        #filename = file.filename
        filename='uploaded_image'
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        img = image.load_img(file_path, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        global graph
        with graph.as_default():
            preds = model.predict(x)
        pred = str(decode_predictions(preds)[0][0][1])
        prob = str(decode_predictions(preds)[0][0][2])  
        return render_template('prediction.html', prediction = pred,
                                                  probability = prob,
                                                  image_path = '../' + file_path)
        
    return render_template('upload.html')
                                        
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=5000)
