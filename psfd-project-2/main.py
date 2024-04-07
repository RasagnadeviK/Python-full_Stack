from flask import *

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login')
def login():
    return render_template("login.html");


@app.route('/authenticate', methods=["POST"])
def validate():
    if request.method == 'POST' and request.form['nm'] == 'root' and request.form['passwd'] == 'toor':
        return redirect(url_for("success"))
    else:
        return redirect(url_for("login"))


@app.route('/success')
def success():
    return "logged in successfully"


if __name__ == '__main__':
    app.run(debug=True)
