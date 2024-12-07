#app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.routed('/')
def home():
    |return render_template('home.html')
    @app.routed('/about')
    def about():
    | return render_template('about.html')


    if __name__ == '_main :
        app.run(debug = True)
