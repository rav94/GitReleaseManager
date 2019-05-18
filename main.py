import os.path
from flask import Flask, render_template, request
from GitRelease import GitRelease
from PropertyReader import PropertyReader

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/release", methods = ['POST'])
def release():
    if request.method == 'POST':
        release_version = request.form['release_id'] 
        new_version = request.form['new_id']
        env_props = PropertyReader().read_properties_file()
        out, error = GitRelease(env_props.get('git_repo_directory'), release_version, new_version).git_release_invoke()
        return render_template("test.html", release_version_val = out, new_version_val = error)

if __name__ == "__main__":
    app.run(debug=True)
