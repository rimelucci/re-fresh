from flask import Flask, render_template, session, redirect
from flask import url_for, request, flash, Markup
import utils

app = Flask(__name__)

# @app.route("/")
# @app.route("/home")
# def home():
#     error = ""
#     return render_template("index.html", error=error)

@app.route("/", methods=["GET","POST"])
def home():
    error= ""
    return render_template("index.html", error=error)

@app.route("/register", methods=["GET", "POST"])
def register():
    username = request.form["username"]
    password = request.form["password"]
    email = request.form["email"]
    #put in the real names of the inputs later
    if utils.check_username(username):
        #if username is usable, then register user
        utils.register_user(username,email,password)
        print utils.fetch_all_users()
        return redirect(url_for("/", error=error))
    else:
        print "error"
        error = "You have entered an unusable username, password, or email."
        return redirect(url_for("/", error=error))

@app.route("/login", methods=["GET","POST"])
def login():
    #GET case
    if request.method == "GET":
        error= ""
        return render_template("register.html", error=error)
    #POST case
    else:
        username = request.form["username"]
        password = request.form["password"]
        if authenticate(username,password):
            #authenticate function
            session['user'] = username
            session.permanent = True
            app.permanent_session_lifetime = timedelta(minutes=5)
            error = "You have successfully logged in!"
            return redirect(url_for("/", error=error))
        #login fails
        else:
            error = "Incorrect Username or Password!"
            return redirect(url_for("/login", error=error))

@app.route("/logout")
def logout():
    session.pop('user', None)
    error = "You have successfully logged out!"
    return redirect(url_for("/", error=error))
 
@app.route("/about")
def about():
    error=""
    return render_template("about.html", error=error)

if __name__ == "__main__":
    app.debug = True
    app.secret_key="secret"
    app.run(host = "0.0.0.0", port = 8000)
