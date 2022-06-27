from flask import Flask, render_template
import random
import requests
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1,10)
    current_year = datetime.now().year
    return render_template("index.html",random_number=random_number, current_year=current_year)

@app.route('/guess/<string:name>')
def name_data(name):

    name = name.title()

    age_response = requests.get(url=f"https://api.agify.io?name={name}")
    age_data = age_response.json()
    age = age_data["age"]

    gender_response = requests.get(url=f"https://api.genderize.io?name={name}")
    gender_data = gender_response.json()
    gender = gender_data["gender"]

    return render_template("guess.html", name=name, age=age, gender=gender )

@app.route('/blog/<num>')
def blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blog_url)
    all_posts = response.json()

    return render_template("blogs.html", posts=all_posts)

if __name__ =="__main__":
    app.run(debug=True)