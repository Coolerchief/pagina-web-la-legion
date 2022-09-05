from flask import Flask, render_template, session, url_for

alfaautoApp = Flask(__name__)

@alfaautoApp.route('/')
def index():
    return render_template('home.html')

if __name__=='__main__':
    alfaautoApp.run(debug=True, port=3300)