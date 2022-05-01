from flask import Flask,request, jsonify, json, render_template, redirect, url_for
# from requests import request
from youtube import *
from perspective import *
# ALTER THE API KEY IN YOUTUBE.PY AND PERSPECTIVE.PY

app = Flask(__name__)

@app.route("/", methods = ['POST','GET'])
def index():
    if request.method == 'POST':

        # getting data from form
        text_analyse = request.form['text_analyse']
        yt_analyse = request.form['yt_analyse']

        print(text_analyse,yt_analyse)
        # performing toxicity analysis on the data received
        if(text_analyse!=""):
            text = analyse_text_req(text_analyse) # returns probability of the text being toxic, insult, profane, threat
            print("text done")
        else:
            text = [0,0,0,0]

        if yt_analyse!="":
            comments = video_comments(yt_analyse)
            yt = analyse_yt_req(comments) # returns percentage of comments which are toxic, insult, profanity and threat, if probability it >70%
        else:
            yt = [0,0,0,0]

        return redirect(url_for('.analyse', text=text,yt=yt))
        # return redirect("/analyse", text=text,yt=yt)
    else:
        return render_template('index.html')

@app.route("/analyse", methods = ['POST','GET'])
def analyse():
    if request.method == 'POST':
        return redirect('/')
    else:

        text = request.args['text']
        yt = request.args['yt']

        return render_template('analyse.html', text=text,yt=yt)


if __name__ == "__main__":
    app.run(debug = True)