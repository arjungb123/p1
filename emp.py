from flask import Flask, render_template,request
from empdata import Employ
app=Flask(__name__)
getemp=Employ()
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/employ')
def data():
    return render_template('emp.html',myemp=getemp)
if(__name__=='__main__'):
    app.run(debug=True)
   