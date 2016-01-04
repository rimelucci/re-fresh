from flask import Flask, render_template, session, redirect
from flask import url_for, request, flash, Markup
import utils

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    username = request.form["username"]
    password = request.form["password"]
    email = request.form["email"]
    #put in the real names of the inputs later
    if utils.check_username(username):
        #if username is usable, then register user
        utils.register_user(username,email,password)
        #print utils.fetch_all_users()
        return redirect(url_for("home"))
    else:
        return redirect(url_for("index"))

@app.route("/login", methods=["GET","POST"])
def login():
    #GET case
    if request.method == "GET":
        return render_template("register.html")
    #POST case
    else:
        username = request.form["username"]
        password = request.form["password"]
        if authenticate(username,password):
            #authenticate function
            session['user'] = username
            session.permanent = True
            app.permanent_session_lifetime = timedelta(minutes=5)
            return redirect("index.html")
        #login fails
        else:
            return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for("/"))
 
@app.route("/reset")
def reset():
    utils.reset()
    print "DATABASE RESET"
    return redirect(url_for("home"))

@app.route("/customerlogin")
def custlogin():
    return render_template("customerlogin.html")




if __name__ == "__main__":
    app.debug = True
    app.secret_key="secret"
    app.run(host = "0.0.0.0", port = 8000)
