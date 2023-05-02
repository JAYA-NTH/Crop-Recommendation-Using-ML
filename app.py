from flask import Flask, render_template, request, jsonify,redirect
#from flask_ngrok import run_with_ngrok
import numpy as np
import pickle
app = Flask(__name__)

model = pickle.load(open('RandomForest.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET','POST'])
def predict():
    v1 = request.form['nitrogen']
    v2 = request.form['phosphorus']
    v3 = request.form['potassium']
    v4 = request.form['temperature']
    v5 = request.form['humidity']
    v6 = request.form['ph']
    v7 = request.form['rainfall']

    prediction = model.predict(np.array([[float(v1),float(v2),float(v3),float(v4),float(v5),float(v6),float(v7)]]))[0]
    print(prediction)
    return render_template('index.html', OUTPUT=prediction)




if __name__ == "__main__":
    app.run(debug=True)