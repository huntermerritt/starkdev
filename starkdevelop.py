from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/elle")
def elle():
    return render_template("elle.html")

@app.route("/hannah")
def hannah():
    return render_template("hannah.html")

@app.route("/kate")
def kate():
    return render_template("kate.html")

@app.route("/plat")
def plat():
    return render_template("platford.html")




if __name__ == '__main__':
    app.run()
