from flask import Flask, render_template, request, redirect
from model.model import predict_pipeline
from model.model import __version__ as model_version
from flask_cors import CORS, cross_origin
import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

cors = CORS(app)

@app.route("/",  methods=["GET", "POST"])
def home():
    result=""
    text = request.form['text']

    result = predict_pipeline(text)

   # print("text",text)
    return  render_template("home.html",result=result )

@app.route("/predict" )
def predict():
    text = request.form['text']

    print("text",text)
    #print("text1",text)
   # language = predict_pipeline(text)
    #print(language)
    #return {"language": language}
    return "hey"

if __name__ =="__main__":
    app.run(debug=True)