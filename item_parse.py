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

# print raw

# for thing in raw:
#     print thing['name'], thing['email'], thing['price'], thing['quantity']

def mongo_feed():
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
    

# <!-- START ROW HERE -->
      # <div class="row">
      #       <div class="col s3 white entry writing">
      #         <center>
      #           <i class="large material-icons">stars</i>
            #     <h5>New Item</h5> NAME OF ITEM
            #     <h7>Store, Distance</h7> STORE, DISTANCE
            #     <hr width="75%" style="margin: 1%">
            #     <b>
            #       $200,000.00 PRICE
            #     </b><br>
            #     <a class="waves-effect waves-light btn info">Add to Cart</a>
            #   </center>
            # </div>

#             <div class="col s3 white entry writing">
#               <center>
#                 <i class="large material-icons">stars</i>
#                 <h5>New Item</h5>
#                 <h7>Store, Distance</h7>
#                 <hr width="75%" style="margin: 1%">
#                 <b>
#                   $200,000.00
#                 </b><br>
#                 <a class="waves-effect waves-light btn info">Add to Cart</a>
#               </center>
#             </div>

#             <div class="col s3 white entry writing">
#               <center>
#                 <i class="large material-icons">stars</i>
#                 <h5>New Item</h5>
#                 <h7>Store, Distance</h7>
#                 <hr width="75%" style="margin: 1%">
#                 <b>
#                   $200,000.00
#                 </b><br>
#                 <a class="waves-effect waves-light btn info">Add to Cart</a>
#               </center>
#             </div>

#             <div class="col s3 white entry writing">
#               <center>
#                 <i class="large material-icons">stars</i>
#                 <h5>New Item</h5>
#                 <h7>Store, Distance</h7>
#                 <hr width="75%" style="margin: 1%">
#                 <b>
#                   $200,000.00
#                 </b><br>
#                 <a class="waves-effect waves-light btn info">Add to Cart</a>
#               </center>
#             </div>
#       </div>
#       <!-- END ROW HERE -->
