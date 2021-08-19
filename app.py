from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('randomForest_model.pkl', 'rb'))


@app.route('/', methods=['GET'])
def Home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')




@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        Age = int(request.form['Age'])
        Final_Weight = int(request.form['Final_Weight'])
        education_num = int(request.form['education_num'])

        marital_status = request.form['marital-status']
        if (marital_status == 'Couple'):
            marital_status = 0
        else:
            credit_history = 1

        relationship = request.form['relationship']
        if (relationship == 'Unmarried'):
            relationship = 0
        elif (relationship == 'Wife'):
            relationship = 1
        elif (relationship == 'Husband'):
            relationship = 2
        elif (relationship == 'Not-in-family'):
            relationship = 3
        elif (relationship == 'Own-child'):
            relationship = 4
        else:
            relationship = 5

        Race = request.form['Race']
        if (Race == 'White'):
            Race = 0
        elif (Race == 'Amer-Indian-Eskimo'):
            Race = 1
        elif (Race == 'Asian-Pac-Islander'):
            Race = 2
        elif (Race == 'Black'):
            Race = 3
        else:
            Race = 4

        Gender = request.form['Gender']
        if (Gender == 'Male'):
            Gender = 1
        else:
            Gender = 0

        capital_gain = request.form['capital_gain']
        if (capital_gain == 'Zero'):
            capital_gain = 0
        else:
            capital_gain = 1

        capital_loss = request.form['capital_loss']
        if (capital_loss == 'Zero'):
            capital_loss = 0
        else:
            capital_loss = 1

        hours_per_week = int(request.form['hours_per_week'])

        country = request.form['country']
        if (country == 'US'):
            country = 1
        else:
            country = 0

        Emplyee_Type = request.form['Emplyee_Type']
        if (Emplyee_Type == 'govt'):
            Emplyee_Type = 0
        elif (Emplyee_Type == 'Private'):
            Emplyee_Type = 1
        elif (Emplyee_Type == 'Self-Employed'):
            Emplyee_Type = 2
        else:
            Emplyee_Type = 3

        prediction = model.predict([[Age, Final_Weight, education_num, marital_status, relationship,
                                     Race, Gender, capital_gain, capital_loss,hours_per_week,
                                     country, Emplyee_Type]])[0]

        return render_template('result.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True, port=9090)
