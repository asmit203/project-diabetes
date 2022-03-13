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
    return "<p>Sign up page</p>"

@app.route("/log_in")
def log_in():
    return "<p>Sign up page</p>"



if __name__=="__main__":
        app.run(debug=True)