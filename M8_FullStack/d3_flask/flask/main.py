from os import name
from flask import Flask, render_template

# components are resuable things

app = Flask(__name__)



@app.route("/") #route request
def index():
    return render_template('index.html', username="Pathi") #the response




if __name__=='__main__':
    app.run(debug = True) #debug shows the errors in terminal