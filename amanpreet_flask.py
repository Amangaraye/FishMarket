



import numpy as np
import pickle
import pandas as pd
from flask import Flask, request
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)

# Loading the trained ML model through Logistic Reression as the pickle file
LR_model = pickle.load(open('LogisticRegresion_FishMarket_model.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('Index_Fish.html')
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = list(map(int,[x for x in request.form.values()]))
    final_features = [np.array(int_features)]
    prediction = LR_model.predict(final_features)

    if prediction[0]==0:
      return render_template('Index_Fish.html', prediction_text='The Fish is Bream')
    elif prediction[0]==1:
      return render_template('Index_Fish.html', prediction_text='The Fish is Parkki')
    elif prediction[0]==2:
      return render_template('Index_Fish.html', prediction_text='The Fish is Perch')
    elif prediction[0]==3:
      return render_template('Index_Fish.html', prediction_text='The Fish is Pike')
    elif prediction[0]==4:
      return render_template('Index_Fish.html', prediction_text='The Fish is Roach')
    elif prediction[0]==5:
      return render_template('Index_Fish.html', prediction_text='The Fish is Smelt')
    else:
      return render_template('Index_Fish.html', prediction_text='The Fish is Whitefish')

#Running the Flask app on local host.
if __name__ == "__main__":
  app.run()
