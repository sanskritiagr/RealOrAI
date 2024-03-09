from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.applications.vgg16 import preprocess_input
import os
from tensorflow.keras.preprocessing import image
import pickle
import joblib


app = Flask(__name__)
# model = joblib.load("model2.pkl")
# model2 = pickle.load(open("model2.pkl", 'rb'))
# model2.save('model.h5')
model = load_model('C:/Users/sansk/Downloads/Projects/ai-v-real-master/model.h5')
target_img = os.path.join(os.getcwd() , 'image')

@app.route('/')
def index_view():
    return render_template('index.html')

#Allow files with extension png, jpg and jpeg
ALLOWED_EXT = set(['jpg' , 'jpeg' , 'png'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXT
           
# Function to load and prepare the image in right shape
def read_image(filename):
    img = load_img(filename, target_size=(32, 32))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return x

@app.route('/predict',methods=['POST'])
def predict():
      
      file = request.files['file']
      if file and allowed_file(file.filename): #Checking file format
          filename = file.filename
          file_path = os.path.join('C:/Users/sansk/Downloads/Projects/ai-v-real-master/data', filename)
          file.save(file_path)
          img = read_image(file_path) #prepressing method
          class_prediction = model.predict(img) 
          # classes_x = np.argmax(class_prediction,axis=1)
          if class_prediction == 0:
            predc = "Real"
          else:
            predc = "Fake"
          #'flower' , 'prob' . 'user_image' these names we have seen in predict.html.
          # print(filename)
          return render_template('predict.html', predc = predc, prob=class_prediction, user_image = filename)
      else:
        return "Unable to read the file. Please check file extension"
        
if __name__ == '__main__':
    app.run()