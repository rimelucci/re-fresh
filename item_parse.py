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
raw = utils.fetch_all_items()

print raw

for thing in raw:
    print thing['name'], thing['email'], thing['price'], thing['quantity']

def create_feed():
    output = ""
    for item in items:
        output += funstring.replace()
    return output
    
