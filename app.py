from pymongo import MongoClient
from flask import Flask, render_template, request
from DB import Forms

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/email', methods=["POST"])
def email_post():
    forms = Forms()
    forms.addData(name= request.form["name"], email= request.form["email"])
    return render_template('email_got.html')

@app.route('/email', methods=["GET"])
def email():
    forms = Forms()
    formsData = forms.getAllData()
    print(forms)
    return render_template('email.html', formsData = formsData)



if __name__ == '__main__':
   app.run()