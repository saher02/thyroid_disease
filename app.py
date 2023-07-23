from flask import Flask,render_template,request, jsonify
import numpy as np
import pickle

model= pickle.load(open('finalmodel.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict_thyroid():
    age = int(request.form.get('age'))
    sex = int(request.form.get('sex'))
    sick = int(request.form.get('sick'))
    pregnant = int(request.form.get('pregnant'))
    thyroidsurgery = int(request.form.get('thyroid surgery'))
    I131_treatment = int(request.form.get('I131 treatment'))
    lithium = int(request.form.get('lithium'))
    goitre = int(request.form.get('goitre'))
    tumor = int(request.form.get('tumor'))
    tsh = float(request.form.get('TSH'))
    t3 = float(request.form.get('T3'))
    tt4 = float(request.form.get('TT4'))
    t4u = float(request.form.get('T4U'))
    fti = float(request.form.get('FTI'))

    result = model.predict(np.array([ age, sex, sick, pregnant, thyroidsurgery,
       I131_treatment, lithium, goitre, tumor, tsh, t3, tt4,
       t4u, fti]).reshape(1, -1))
    print('output: ',result)

    if result == 1:
        output = " Unfortunately, You have thyroid :("
    else:
        output = "Bravo you do not have thyroid :)"

    return render_template('index.html',result=output)
    
if __name__ == '__main__':
    #app.run(debug=True) for local run
    app.run(host="0.0.0.0", port=8080, debug=True)