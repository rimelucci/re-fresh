from flask import Flask, render_template, session, redirect, url_for, request, flash, Markup

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", session=session)



if __name__ == "__main__":

    util.initializeTables()
    app.debug = True
    app.secret_key="secret"
    app.run(host = "0.0.0.0", port = 8000)
