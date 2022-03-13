from flask import Flask

app = Flask(__name__)

@app.route("/")
def home_page():
    return "<p>Web App to check for Diabetes</p>"

@app.route("/sign_up")
def sign_up():
    return "<p>Sign up page</p>"

@app.route("/log_in")
def log_in():
    return "<p>Sign up page</p>"



if __name__=="__main__":
        app.run(debug=True)