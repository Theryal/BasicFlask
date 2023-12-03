from flask import Flask, render_template
import requests

app = Flask(__name__)




@app.route('/')
def home():
    return "Hello, write '/guess/(your name)' in the address bar!"


@app.route('/guess/<name>')
def guess(name):
    gender_response = requests.get(url=f"https://api.genderize.io?name={name}")
    gender = gender_response.json()['gender']
    age_response = requests.get(url=f"https://api.agify.io?name={name}")
    age = age_response.json()['age']
    return render_template("index.html", n=name, gen=gender, num=age)


if __name__ == "__main__":
    app.run(debug=True)
