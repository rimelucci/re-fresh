import utils

funstring="""
 <div class="row">
            <div class="col s3 white entry writing">
              <center>
                <i class="large material-icons">stars</i>
                <h5>New Item</h5>
                <h7>Store, Distance</h7>
                <hr width="75%" style="margin: 1%">
                <b>
                  $200,000.00
                </b><br>
                <a class="waves-effect waves-light btn info">Add to Cart</a>
              </center>
            </div>
    </div>
            """

items = []

# print raw

# for thing in raw:
#     print thing['name'], thing['email'], thing['price'], thing['quantity']

def mongo_feed():
    raw = utils.fetch_all_items()
    counter = 0
    output = ""
    for item in raw:
        if (counter == 0):
            output +="""
            <div class="row">
            <div class="col s3 white entry writing">
            <center>
            <i class="large material-icons">stars</i>"""
            
            output = output + "<h5>" + item['name'] +", qty: " + str(item['quantity']) + "</h5><h7>" + item['email'] + """, Distance</h7>
            <hr width="75%" style="margin: 1%"><b>$""" + item['price'] + """</b><br>
            <a class="waves-effect waves-light btn info">Add to Cart</a>
            </center>
            </div>
            """
        if ((counter > 0)&(counter < 3)):
            output +="""
            <div class="col s3 white entry writing">
            <center>
            <i class="large material-icons">stars</i>"""
            
            output = output + "<h5>" + item['name'] + ", qty: " + str(item['quantity']) + "</h5><h7>" + item['email'] + """, Distance</h7>
            <hr width="75%" style="margin: 1%"><b>$""" + item['price'] + """</b><br>
            <a class="waves-effect waves-light btn info">Add to Cart</a>
            </center>
            </div>
            """
        if (counter == 3):
            output +="""
            <div class="col s3 white entry writing">
            <center>
            <i class="large material-icons">stars</i>"""
            
            output = output + "<h5>" + item['name'] + ", qty: " + str(item['quantity']) + "</h5><h7>" + item['email'] + """, Distance</h7>
            <hr width="75%" style="margin: 1%"><b>$""" + item['price'] + """</b><br>
            <a class="waves-effect waves-light btn info">Add to Cart</a>
            </center>
            </div>
            """
            output += "</div>"
            counter = -1
            
        counter += 1

    if (counter != 3):
        output += "</div>"

    return output

def create_feed():
    output = ""
    for item in items:
        output += funstring.replace()
    return output



def create_cart(email):
    rawfeed = utils.get_user_cart(email)
    output = """
    <div id="cart" class="cart-onscreen" style="display: none">
    <h3>Your Cart</h3>
    """
    for item in rawfeed:
        output = output + """
        <div class="row item">
        <h5>""" + item['name'] +"""</h5>
        <i class="material-icons">stars</i>
        <p style="float: right">""" + """
        </p>
        </div>
        """
    output += """<center><a class="waves-effect waves-light btn" >
    Proceed to Checkout</a>
    </center></div>"""
        
    return output

    # print create_cart("derricklui@gmail.com")

    # <div id="cart" class="cart-onscreen" style="display: none">
    #   <h3>Your Cart</h3>
    # <div class="row item">
    #   <h5>Item Name</h5>
    #   <i class="material-icons">stars</i>
    #   <p style="float: right">
    #     $200,000.00
    #   </p>
    # </div>
  #   <div class="row item">
  #     <h5>Item Name</h5>
  #     <i class="material-icons">stars</i>
  #     <p style="float: right">
  #       $200,000.00
  #     </p>
  #   </div>
  #   <div class="row item">
  #     <h5>Item Name</h5>
  #     <i class="material-icons">stars</i>
  #     <p style="float: right">
  #       $200,000.00
  #     </p>
  #   </div>
  #   <div class="row item">
  #     <h5>Item Name</h5>
  #     <i class="material-icons">stars</i>
  #     <p style="float: right">
  #       $200,000.00
  #     </p>
  #   </div>
    
  # </div>
