from flask import Flask, render_template, session, redirect
from flask import url_for, request, flash, Markup
import utils
import stripe
import os
import item_parse

# stripe_keys = {
#     'secret_key': os.environ['SECRET_KEY'],
#     'publishable_key': os.environ['PUBLISHABLE_KEY']
# }

app = Flask(__name__)

@app.route("/")
def index():
    if 'user' in session:
        if session['user'] == 0:
            return redirect(url_for("feed"))
        else:
            return redirect(url_for("additem"))
    else:
        return render_template("index.html")

@app.route("/customerregister", methods=["GET", "POST"])
def customerregister():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        if utils.check_username(username) and utils.register_user(username,email,password):
            #if username is usable, then register user
            #print utils.fetch_all_users()
            return redirect(url_for("customerlogin"))
        else:
            return redirect(url_for("customerregister"))
    #GET case
    else:
        return render_template("customerregister.html")

@app.route("/customerlogin", methods=["GET","POST"])
def customerlogin():
    #GET case
    if request.method == "GET":
        return render_template("customerlogin.html")
    #POST case
    else:
        username = request.form["username"]
        password = request.form["password"]
        if utils.authenticate_user(username,password):
            #authenticate function
            session['user'] = 0
            session['name'] = username
            #session.permanent = True
            #app.permanent_session_lifetime = timedelta(minutes=5)
            return redirect(url_for("index"))
        #login fails
        else:
            return redirect(url_for("customerlogin"))

@app.route("/storeregister", methods=["GET","POST"])
def storeregister():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        if utils.check_store(username) and utils.register_store(username,email,password):
            #if username for store is usable, then register store
            #print utils.fetch_all_storess()
            return redirect(url_for("storelogin"))
        else:
            return redirect(url_for("storeregister"))
    #GET case
    else:
        return render_template("storeregister.html")

@app.route("/storelogin", methods=["GET","POST"])
def storelogin():
    #GET case
    if request.method == "GET":
        return render_template("storelogin.html")
    #POST case
    else:
        username = request.form["username"]
        password = request.form["password"]
        if utils.authenticate_store(username,password):
            #authenticate function
            session['user'] = 1
            session['name'] = username
            #session.permanent = True
            #app.permanent_session_lifetime = timedelta(minutes=5)
            return redirect(url_for("additem"))
        #login fails
        else:
            flash("Your email and password do not match")
            return redirect(url_for("storelogin"))

@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for("index"))

@app.route("/feed")
def feed():
    mongofeed = item_parse.mongo_feed()
    mongocart = item_parse.create_cart(session['user'])
    return render_template("feed.html",feed = mongofeed,cart = mongocart,username = session['name'])


@app.route("/reset")
def reset():
    utils.reset()
    print "DATABASE RESET"
    return redirect(url_for("logout"))

@app.route('/test', methods=["GET", "POST"])
def test():
    if request.method == "GET":
        return render_template('testpage.html', key=stripe_keys['publishable_key'])
    # else:
    #     # Insert code here: grabbing dollar amount from database
    #     # and sending it into the flask "/charge" route
    #     # to add custom payment amounts

    #     return render_template('testpage.html', key=stripe_keys['publishable_key'])


@app.route('/charge', methods=['POST'])
def charge():
  amount = 9900

  customer = stripe.Customer.create(
      email='customer@example.com',
      card=request.form['stripeToken']
  )

  charge = stripe.Charge.create(
      customer=customer.id,
      amount=amount,
      currency='usd',
      description='Flask Charge'
  )

  return render_template('testcharge.html', amount=amount)

@app.route('/settings')
def settings():
    return render_template('settings.html', username = session['name'])


@app.route('/additem', methods = ["GET","POST"])
def additem():
    if request.method == 'POST':
        product = request.form['productname']
        price = request.form['price']
        quantity = request.form['quantity']
        utils.register_item(product, quantity, price, session['name'])
        return redirect(url_for('feed'))
    else:
        return render_template('additem.html')



if __name__ == "__main__":
    app.debug = True
    app.secret_key="secret"
    app.run(host = "0.0.0.0", port = 8000)
