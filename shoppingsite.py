"""Ubermelon shopping application Flask server.

Provides web interface for browsing melons, seeing detail about a melon, and
put melons in a shopping cart.

Authors: Joel Burton, Christian Fernandez, Meggie Mahnken.
"""


from flask import Flask, render_template, redirect, flash, session, request
import jinja2

import melons


app = Flask(__name__)

# Need to use Flask sessioning features

app.secret_key = 'this-should-be-something-unguessable'

# Normally, if you refer to an undefined variable in a Jinja template,
# Jinja silently ignores this. This makes debugging difficult, so we'll
# set an attribute of the Jinja environment that says to make this an
# error.

app.jinja_env.undefined = jinja2.StrictUndefined


@app.route("/")
def index():
    """Return homepage."""

    return render_template("homepage.html")


@app.route("/melons")
def list_melons():
    """Return page showing all the melons ubermelon has to offer"""

    melon_list = melons.get_all()
    return render_template("all_melons.html",
                           melon_list=melon_list)


@app.route("/melon/<int:melon_id>")
def show_melon(melon_id):
    """Return page showing the details of a given melon.

    Show all info about a melon. Also, provide a button to buy that melon.
    """

    melon = melons.get_by_id(melon_id)
    print melon
    return render_template("melon_details.html",
                           display_melon=melon)


@app.route("/cart")
def shopping_cart():
    """Display content of shopping cart."""

    # TODO: Display the contents of the shopping cart.

    # The logic here will be something like:
    #
    # - get the list-of-ids-of-melons from the session cart
    # - loop over this list:
    #   - keep track of information about melon types in the cart
    #   - keep track of the total amt ordered for a melon-type
    #   - keep track of the total amt of the entire order
    # - hand to the template the total order cost and the list of melon types

    # creates an empty dictionary to store information about each 
    # melon in the specific user's cart
    cart = {}

    # creates a list of id's of melon's in the user's cart
    # if the cart is empty, the list will default to []
    melon_ids_in_cart = session.get("cart", [])

    # iterates through the melon id's in cart to update quantities
    # keeps track of total price for each melon
    for melon_id in melon_ids_in_cart:

        # if the melon is not already in the cart, create a key of melon id
        # the value is a dictionary containing melon info
        if melon_id not in cart:
            melon_obj = melons.get_by_id(melon_id)
            cart[melon_id] = {
                "melon_name": melon_obj.common_name,
                "qty_ordered": 1,
                "unit_price": melon_obj.price,
                "total_price": melon_obj.price,
            }
            
        # if melon is already in cart, increment quantity and total cost
        else:
            cart[melon_id]["qty_ordered"] += 1
            cart[melon_id]["total_price"] = (
                cart[melon_id]["qty_ordered"] * cart[melon_id]["unit_price"])

        # formats numerical values as monetary strings in a new key: value
        # pair in the melon dictionary we created above
        cart[melon_id]["unit_price_str"] = "${:,.2f}".format(
            cart[melon_id]["unit_price"])
        cart[melon_id]["total_price_str"] = "${:,.2f}".format(
            cart[melon_id]["total_price"])

    # initialize variable to count total cost        
    total = 0

    # for every melon in cart, add the total price to the total
    for melon in cart:
        total += cart[melon]["total_price"]

    total = "${:,.2f}".format(total)

    return render_template("cart.html", cart=cart, total=total)


@app.route("/add_to_cart/<int:id>")
def add_to_cart(id):
    """Add a melon to cart and redirect to shopping cart page.

    When a melon is added to the cart, redirect browser to the shopping cart
    page and display a confirmation message: 'Successfully added to cart'.
    """

    # TODO: Finish shopping cart functionality

    # The logic here should be something like:
    #
    # - add the id of the melon they bought to the cart in the session

    if 'cart' in session:
        session["cart"].append(id)
    else: 
        session["cart"] = []
        session["cart"].append(id)

    flash("The melon was successfully added to your cart.")
    

    return redirect("/cart")


@app.route("/login", methods=["GET"])
def show_login():
    """Show login form."""

    return render_template("login.html")


@app.route("/login", methods=["POST"])
def process_login():
    """Log user into site.

    Find the user's login credentials located in the 'request.form'
    dictionary, look up the user, and store them in the session.
    """

    # TODO: Need to implement this!
    user_email = request.form.get("email")
    user_password = request.form.get("password")



    return "hi"


@app.route("/checkout")
def checkout():
    """Checkout customer, process payment, and ship melons."""

    # For now, we'll just provide a warning. Completing this is beyond the
    # scope of this exercise.

    flash("Sorry! Checkout will be implemented in a future version.")
    return redirect("/melons")


if __name__ == "__main__":
    app.run(debug=True)
