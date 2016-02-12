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
            flash('You have successfully registered a customer account')
            return redirect(url_for("customerlogin"))
        else:
            flash("Your email and password do not match")
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
            flash('You have succesfully logged in as ' + username)
            return redirect(url_for("index"))
        #login fails
        else:
            flash('Register failed')
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
            flash('You have successfully registered a store account')
            return redirect(url_for("storelogin"))
        else:
            flash('Register failed')
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
            flash('You have successfully registered a store account')
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
    if session['user'] == 0:
        redirect(url_for("feed"))
    if request.method == 'POST':
        product = request.form['productname']
        price = request.form['price']
        quantity = request.form['quantity']
        utils.register_item(product, quantity, price, session['name'])
        return redirect(url_for('feed'))
    else:
        return render_template('additem.html')


@app.route('/add/<itemname>')
def add():
    utils.purchase_item(itemname)
    return redirect(url_for('feed'))

@app.route('/info/<itemname>')
def info(itemName=""):
    #function that returns info from the databases
    information = utils.get_item_info(session[name], itemName)
    popUpWindowCode = """<!--This serves as the darkening agent for individual item view -->
      <div class="view-cover"></div>
      <!-- End cover here -->

          <div id="item-view" class="writing">
            <a href="#" id="close"><span class="glyphicon glyphicon-remove" aria-hidden="true" style="float: right"></span></a>
            <div class="row">
              <div class="col s6">
                <img src="http://www.dineoncampus.com/tools/contentImages/image/turkeysub2.jpg" id="item-image">
              </div>

              <div class="col s6">
                <center>
                  <h1>""" + information[0] + """</h1>
                  <h5>Provider Name, Address goes here</h5>
                  <h3>"""+ information[1] +"""</h3> <!--PRICE GOES HERE-->
                  <hr color="black" width="75%">
                  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent facilisis tristique ante, eget lobortis erat ullamcorper vel. Fusce imperdiet faucibus nunc id lobortis.</p>
                  <hr color="black" width="75%">
                </center>
                <h6>Buy it now!</h6>
                <form class="" action="index.html" method="post">
                  <div class="row">

                    <div class="input-field col s4">
                      Quantity
                      <select name="quantity" class="form-control">
                        <option>1</option>
                        <option>2</option>
                        <option>3</option>
                        <option>4</option>
                        <option>5</option>
                      </select>
                    </div>
                  </div>

                    <div class="row">
                        <div class="input-field col s4">
                              <a class="waves-effect waves-light btn">Add to Cart</a>
                        </div>

                        <div class="input-field col s4 offset-s1">
                              <a class="waves-effect waves-light btn">Get Directions</a>
                        </div>
                      </div>
                </form>
              </div>
            </div>
          </div>
        <!--END CRAPPY CODE -->"""
    print information[0]
    return redirect(url_for("feed"), popUpWindowCode = popUpWindowCode)


if __name__ == "__main__":
    app.debug = True
    app.secret_key="secret"
    app.run(host = "0.0.0.0", port = 8000)
