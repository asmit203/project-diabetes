from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('index.html')
    
@app.route("/team")
def team_page():
    return render_template('team.html')

@app.route("/sign_up")
def sign_up():
    return render_template('sign_up.html')

@app.route("/log_in")
def log_in():
    return render_template('log_in.html')

@app.route("/check")
def check():
    return render_template('check.html')

if __name__=="__main__":
        app.run(debug=True)