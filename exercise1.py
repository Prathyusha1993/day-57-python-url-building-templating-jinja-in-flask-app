from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/guess/<send_name>')
def home(send_name):
    response = requests.get(f'https://api.agify.io?name={send_name}')
    # print(response["name"])
    data = response.json()
    my_name = data['name']
    my_age = data['age']
    response2 = requests.get(f'https://api.genderize.io?name={send_name}')
    data2 = response2.json()
    my_gender = data2['gender']
    return render_template('index2.html', name=my_name, age=my_age, gender=my_gender)



if __name__ == '__main__':
    app.run(debug=True)