from flask import Flask, render_template, request

app = Flask(__name__)

UPLOAD_FOLDER = '/Users/Hunter/PycharmProjects/starkdevelop/static'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def start():
    return render_template("builder.html")

@app.route("/create", methods=["GET", "POST"])
def create():
    title = request.args.get("title")

    description = request.args.get("description")

    about = request.args.get("about")

    service1 = request.args.get("service1")
    description1 = request.args.get("description1")

    service2 = request.args.get("service2")
    description2 = request.args.get("description2")

    service3 = request.args.get("service3")
    description3 = request.args.get("description3")

    email = request.args.get("email")

    f1 = request.files['file1']

    f1.save(f1.filename + str(title))

    f2 = request.files['file2']

    f2.save(f2.filename + str(title))

    f3 = request.files['file3']

    f3.save(f3.filename + str(title))

    f4 = request.files['file4']

    f4.save(f4.filename + str(title))

    logofile = request.files['logofile']

    logofile.save(logofile.filename + str(title))

    aboutfile = request.files['aboutfile']

    aboutfile.save(aboutfile.filename + str(title))





    return render_template("temp.html", title=title, description=description, about=about, service1=service1, description1=description1, service2=service2, description2=description2, service3=service3, description3=description3, email=email)

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
