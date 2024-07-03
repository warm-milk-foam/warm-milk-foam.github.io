from flask import Flask, render_template
import requests
app = Flask(__name__, static_folder='C:/Users/student/Downloads/hello_flask/static', template_folder='C:/Users/student/Downloads/hello_flask/templates')

@app.route("/")
def home():
  return render_template('index.html')
  
if __name__ == "__main__":
  app.run(debug=True)
