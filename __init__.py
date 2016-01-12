from flask import Flask, render_template, session, redirect
from flask import url_for, request, flash, Markup
import utils
import stripe

app = Flask(__name__)

@app.route("/")
def index():
    if 'user' in session:
        return render_template("feed.html")
    else:
        return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        if utils.check_username(username):
            #if username is usable, then register user
            utils.register_user(username,email,password)
            #print utils.fetch_all_users()
            flash('You have successfully registered a customer account')
            return redirect(url_for("index"))
        else:
            flash('Register failed')
            return redirect(url_for("register"))
    #GET case
    else:
        return render_template("register.html")

@app.route("/customerlogin", methods=["GET","POST"])
def customer_login():
    #GET case
    if request.method == "GET":
        return render_template("customerlogin.html")
    #POST case
    else:
        username = request.form["username"]
        password = request.form["password"]
        if utils.authenticate_user(username,password):
            #authenticate function
            session['user'] = username
            #session.permanent = True
            #app.permanent_session_lifetime = timedelta(minutes=5)
            flash('You have succesfully logged in as ' + username)
            return redirect(url_for("index"))
        #login fails
        else:
            flash("Your email and password do not match")
            return redirect(url_for("customer_login"))

@app.route("/logout")
def logout():
    session.pop('user', None)
    flash("You have successfully logged out of your account")
    return redirect(url_for("index"))

@app.route("/feed")
def feed():
    return render_template("feed.html")

 
@app.route("/reset")
def reset():
    utils.reset()
    print "DATABASE RESET"
    return redirect(url_for("logout"))

@app.route("/test", methods=["GET","POST"])
def testpage():
    if request.method == "POST":
        token = request.form["stripeToken"]
        flash(token)
        return render_template("testpage.html")
    return render_template("testpage.html")


if __name__ == "__main__":
    app.debug = True
    app.secret_key="secret"
    app.run(host = "0.0.0.0", port = 8000)
