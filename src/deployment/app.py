import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import importlib.util, os
import pandas as pd


# Get current path from where script is executed
if os.name == 'nt':
    sep = '\\'
elif os.name == 'posix':
    sep = '/'
else:
    print(f'What is this OS? {os.name}')

path = os.getcwd()
pathToSrc =  path[:-len(f'deployment')]
pathToGDrive =  path[:-len(f'Code{sep}src{sep}project_CSP_MATH_571')]
path_datasets = pathToGDrive + f'DataSets{sep}'

pathToDataSet = pathToGDrive + f'DataSets{sep}' + dataSetName
df = pd.read_csv('dataset_final.csv')

#MapGenerator Lib
path_maps = pathToSrc + f'{sep}mapGeneration{sep}mapGeneration.py'
spec = importlib.util.spec_from_file_location("mapGeneration", path_maps)
mp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mp)


app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])


def predict():


    # Get values from form.
    date = getDate from request.form.values:

    row = df[date, ]
        
    # Transform to array X
    X = model_name_TransformDataToX(row)


    # Predict
    model = model_name_Load()
    Y = model.predict(X)
    #prediction = np.random.randint(1,200,77)
    # Create map

    result = model_name_TransformYToResult(Y)

    # Create map
    result = mp.mapGenerator(prediction, saveByte=True)    

    result = str(result)[2:-1]

    return render_template('predict.html', result=result)


# For requests and JSON 
@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True)