from flask import Flask
from flask import Flask, render_template
import requests

app = Flask(__name__, static_folder="C:/Users/XXXXXXXXXX/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/flask_website_ingo", template_folder='C:/Users/XXXXXXXXXX/OneDrive - XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx/flask_website_ingo')


@app.route("/")
def home():
  return render_template('home.html')

if __name__ == "__main__":
  app.run()
