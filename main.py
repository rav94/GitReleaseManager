from flask import Flask, render_template
from GitRelease import GitRelease

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/call_git_release")
def call_git_release():
    path = 'TEST'
    release = '7.1.2'
    my_char, my_release = GitRelease(path, release).test()
    return render_template("test.html", value=my_char, value1=my_release)

if __name__ == "__main__":
    app.run(debug=True)
