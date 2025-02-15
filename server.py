from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    random_number = random.randint(1, 10)
    current_year = datetime.now().year
    return render_template('index.html', num=random_number, year=current_year)

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    response3 = requests.get('https://api.npoint.io/d3956500e07e4947dcc2')
    all_post = response3.json()
    return render_template('blog.html', posts=all_post)


if __name__ == '__main__':
    app.run(debug=True)