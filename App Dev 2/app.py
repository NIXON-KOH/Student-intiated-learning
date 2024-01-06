from flask import Flask, request, render_template, redirect
import shelve 
from product import Products
from user import User

app = Flask(__name__)

def initialiser():
    global items
    items = []
    with shelve.open("Database/products") as f:
        for i in f:
            #name, pricing, categories, rating, image
            globals()[f[i]["name"]] = Products(
                f[i]["name"],
                f[i]["pricing"],
                f[i]["categories"],
                f[i]["Gender"],
                f[i]["color"],
                f[i]["type"],
                f[i]["rating"],
                f[i]["image"]
            )
            items.append(f[i]["name"])

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/login",methods=["GET","POST"])
def login():
    global user
    if request.method == "POST":
        with shelve.open("Database/user") as f:
            for i in f:
                if request.form.get("name") == f[i]["name"] and request.form.get("password") == f[i]["password"]:
                    user = User(f[i]["name"],f[i]["password"],f[i]["email"],f[i]["role"],f[i]["cart"])
                    return redirect("shop.html")
    return render_template("login.html")

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method == "POST":
        with shelve.open("Database/user") as f:
            x = 1
            for i in f:
                x += 1
            f[str(x)] = {
                "name" : request.form.get('name'),
                "password" : request.form.get("password"),
                "email" : request.form.get("email"),
                "role" : "Cust"
            }
            user = User(f[str(x)]["name"],f[str(x)]["password"],f[str(x)]["email"],f[str(x)]["role"])
    return render_template("")

@app.route("/cart")
def cart():
    
    return render_template("cart.html")

@app.route("/<item>")
def item(item):
    image = f'''    <div class="img-container">
           <div class="img-magnifier-container">
        <img id="myimage" src="/static/assets/{globals()[item].get_image()}" style="width:20vw;height:auto;">
      </div> 
    </div>
    '''
    return render_template("item.html", image=image, price=globals()[item].get_pricing(), rating=globals()[item].get_rating(), name=globals()[item].get_name())

@app.route("/shop")
def shop():
    cards = ""
    x = 1
    for i in items:

        card1 = f'''
            <div class="grid-item">
        <p><img src="static/assets/{globals()[i].get_image()}" alt="{globals()[i].get_name()}"></p>'''
        card2 = "<h4><a href="+"{{ url_for('item',item="+ f"{globals()[i].get_name()}" +") }}"+f" >{globals()[i].get_name()}</a></h4>"
        maximum = 5
        rating = globals()[i].get_rating()
        filled = rating*'<span class="bi-star-fill"></span>'
        empty = (maximum - rating)*'<span class="bi bi-star" style="font-size:100%;"></span>'
        card3 = filled+empty
        card4 =  f'''<p>SGD {globals()[i].get_pricing()}</p>
      </div>
        '''     

        card = card1+card2+card3+card4
        cards += card
        x += 1
    print(cards)
    return render_template("shop.html",all_cards=cards)
if __name__ == "__main__":
    initialiser()
    app.run(debug=True)


