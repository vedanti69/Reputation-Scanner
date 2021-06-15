"""
To launch the engine (starting point of project).
"""
from flask import Flask, render_template, request, url_for
from api import getData
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():

    return render_template('home.html')

@app.route('/search',methods=['GET','POST'])
def search():
    data=getData(request.form['search'])
    return render_template('result.html',result= data)
if __name__=="__main__":
    app.run(port=4242)