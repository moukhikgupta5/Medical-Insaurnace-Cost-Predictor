import numpy as np
from flask import Flask, render_template,request
import pickle#Initialize the flask App
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
print(model.predict([np.asarray((31,1,25.74,0,1,0))]))

# age sex(m0 f1) bmi children smoker region 'southeast':0,'southwest':1,'northeast':2,'northwest':3

# default page of our web-app
@app.route('/')
def home():
    return render_template('index.html')
    # prediction = model.predict([np.asarray((31,1,25.74,0,1,0))])
    # output = round(prediction[0], 2) 
    # output = 30
    # return render_template('index.html', prediction_text='Cost :{}'.format(output))

#To use the predict button in our web-app
@app.route('/predict',methods=['POST'])
def predict():
    print("hello")
    age = request.form.get('age');
    bmi = request.form.get('bmi');
    gender = request.form.get('gender');
    smoker = request.form.get('smoker');
    children = request.form.get('children');
    region = request.form.get('region');
    
    int_features = []
    int_features.append(age)
    int_features.append(bmi)
    int_features.append(gender)
    int_features.append(smoker)
    int_features.append(children)
    int_features.append(region)
    print(int_features)
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2) 
    return render_template('prediction.html', prediction_text='{}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)