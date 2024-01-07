from flask import Flask, render_template, request, redirect,url_for
from user import Customer, Admin
from product import Product, Rewards
import shelve, json, random, datetime, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def initate():
    global Products,reward
    reward = []
    Products = []
    with shelve.open("Databases/product") as f:
        for i in f:
            #id_, name,Image, Stocks, Desc, Type, Status,categories,RetailCost,gender,ListCost,reviews
            #Reads Product data
            if f[i]["type"] == "product":
                globals()[f[i]['name']] = Product(
                    i,
                    f[i]["name"],
                    f[i]["image"],
                    f[i]["stocks"],
                    f[i]["desc"],
                    f[i]["points"],
                    f[i]["type"],
                    f[i]["categories"],
                    f[i]["RetailCost"],
                    f[i]["gender"],
                    f[i]["ListCost"],
                    f[i]["reviews"]
                )
                Products.append(f[i]['name'])
            elif f[i]["type"] == "rewards":
                globals()[f[i]["name"]] = Rewards(
                    i,
                    f[i]["name"],
                    f[i]["image"],
                    f[i]["stocks"],
                    f[i]["desc"],
                    f[i]["type"],
                    f[i]["Status"],
                    f[i]["points"]
                )
                reward.append(f[i]['name'])

def chatbot(query):
    lol = "Sorry i could not get that."
    intent = "N/A"
    with open("chatbot.json") as f:
        data = json.load(f)
        f.close()
    for i in range(len(data)):
        for n in data[i]["patterns"]:
            if query.lower() in n.lower():
                return random.choice(data[i]["responses"]),data[i]["tag"]
    return lol,intent
                                    

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def lobby():
    if request.method == "POST":
        query = request.form['chat']
        chatbot(query)
    
    return render_template("index.html")


@app.route("/rewards")
def rewards():
    return render_template("reward.html")

@app.route("/login",methods=["GET","POST"])
def authenticate():
    if request.method == "POST":
        username = request.form['name']
        password = request.form['password']
        global user
        with shelve.open("Databases/user") as f:
            for i in f:
                if f[i]['username'] == username and f[i]["password"] == password:
                    if f[i]["role"] == "admin":
                        user = Admin(i,f[i]["role"],f[i]["username"],f[i]["JoinDate"],f[i]["password"],f[i]["image"],f[i]["email"])
                    elif f[i]["role"] == "user":
                        user = Customer(i,"user",f[i]["username"],f[i]["JoinDate"],f[i]["password"],f[i]["image"],f[i]["email"],f[i]["address"],f[i]["Payment"],f[i]["cart"],f[i]["History"],f[i]["point"])
                    else:
                        print("ERROR !!!!")
                    return redirect("dashboard")
                else:
                    return redirect(url_for('home'))
    return render_template("login.html")

@app.route("/user")
def registration():
    #Read User data
    return render_template("", uname=user.get_name(),pwd=user.get_Password(),image=user.get_image(),email=user.get_Email(),addr=user.get_Address(),cart=user.get_cart(),hist=user.get_History(),joindate=user.get_JoinDate(),points=user.get_Points())


@app.route("/registration",methods=["GET",'POST'])
def registration():
    if request.method == "POST":
        username = request.form['name']
        password = request.form['password']
        email = request.form['email']
        address = request.form['address']

        with shelve.open('database') as f: 
            x = 1
            for i in f:
                if f[i]['username'] == username:
                    return redirect(url_for("register.html"))
                x += 1
            #Create User Data
            f[str(x)] = {
                "name" : username,
                "password" : password,
                "role" : "user",
                "image" : f"{str(x)}.jpg",
                "email" : email,
                "address" : address,
                "History" : {},
                "Payment" : {},
                "JoinDate" : datetime.datetime.today().strftime('%d-%m-%Y'),
                "points" : 0,
                "cart" : {}
                }
            
        #Email confirmation
        #Reads user data
        smtp_user = 'appdevrulez2@gmail.com'
        smtp_password = 'pepermoflhvbytgw'
        destination_user =  email
        server = 'smtp.gmail.com'
        port = 587
        msg = MIMEMultipart("alternative")
        msg["Subject"] = 'Registration confirmation'
        msg["From"] = smtp_user
        msg["To"] = destination_user
        msg.attach(MIMEText('Welcome! \nThis email confirms your registration with ', 'plain'))

        s = smtplib.SMTP(server, port)
        s.ehlo()
        s.starttls()
        s.login(smtp_user, smtp_password)
        s.sendmail(smtp_user, destination_user, msg.as_string())
        s.quit()

        return redirect('dashboard.html')
    return render_template("register.html")

@app.route("/cart",methods=["GET",'POST'])
def cart():
    if request.method == "POST":
        # email confirmation
        with shelve.open("Databases/product") as f:
            f[Customer.get_id_][Customer.get_Cart] = {}
        smtp_user = 'appdevrulez2@gmail.com'
        smtp_password = 'pepermoflhvbytgw'
        destination_user =  Customer.get_email()
        server = 'smtp.gmail.com'
        port = 587

        msg = MIMEMultipart("alternative")
        msg["Subject"] = 'Order confirmation'
        msg["From"] = smtp_user
        msg["To"] = destination_user
        msg.attach(MIMEText('Welcome! \nThis email confirms your order', 'plain'))

        s = smtplib.SMTP(server, port)
        s.ehlo()
        s.starttls()
        s.login(smtp_user, smtp_password)
        s.sendmail(smtp_user, destination_user, msg.as_string())
        s.quit()
    return render_template("cart.html",user.get_Cart())


@app.route("/shop",method=["POST","GET"])
def shop():
    if request.method == "POST":
        #Button will all have same name but different values
        #adds items to cart
        Customer.set_Cart = request.form["item"]
        with shelve.open("Databases/user") as f:
            for i in f:
                if f[i]["name"] == Customer.get_name():
                    f[i]["cart"].append(request.form["item"])   
        with shelve.open("Databases/product") as f:
            for i in f:
                if f[i]["name"] == request.form['item']:
                    f[i]["size"][request.form["size"]] = f[i]["size"][request.form["size"]] - 1

    cards = ""
    for i in Products:
        card_part1 = f'''<form action="test.html">
        <div class="card">
            <img src="Assets/{i.replace(" ","_")}.jpeg" alt="{i.replace(" ","_")}.jpeg" style="width:100%">
            <div class="row1">
                <h1>{i}</h1>
                <span class="icon-cart">
                    <button><i class="fa fa-shopping-cart fa-2x" id="icon-cart"></i></button>
                </span>
            </div>
            <div class="row2">
                <label for="size">Size:</label>
                <select id="size" name="size">
                '''
        sizings = ["S","M","L","XL","XXL"]
        card_part_2 = ""
        for n in sizings:
            if (globals()[i].get_Stocks()).get(n) != 0:
                card_part_2 += f"<option value='{n}'>{n}</option>"
            else:
                card_part_2 += f"<option value='{n}' disabled>{n}</option>"
        card_part_3 = f'''</select>
            </div>
            <div class="row3">
                <h2 class="price">SGD {globals()[i].get_RetailCost()}</h2>
            </div>
        </div>
    </form>'''
        card = card_part1+card_part_2+card_part_3
        cards += card
    return render_template("shop.html",cards=cards)     

@app.route("/admin-create-product",methods=["GET","POST"])
def create_product():
    #Creating product
    if request.method=="POST":
        with shelve.open("Databases/product") as f:
            for i in f:
                n = i
            f[str(n)] = {
                    n,
                    request.form["name"],
                    request.form["image"],
                    request.form["stocks"],
                    request.form["desc"],
                    request.form["points"],
                    request.form["type"],
                    request.form["categories"],
                    request.form["RetailCost"],
                    request.form["gender"],
                    request.form["ListCost"],
                    request.form["reviews"]
            }
            globals()[request.form["name"]] = Product(
                    n,
                    request.form["name"],
                    request.form["image"],
                    request.form["stocks"],
                    request.form["desc"],
                    request.form["points"],
                    request.form["type"],
                    request.form["categories"],
                    request.form["RetailCost"],
                    request.form["gender"],
                    request.form["ListCost"],
                    request.form["reviews"]
            )
            Products.append(request.form["name"])
            return redirect("/admin")
    return render_template("")

@app.route("/admin-rewards",methods=["POST","GET"])
def admin_rewards():
    if request.method == "POST":
        pass

    return render_template("")

@app.route("/admin-rewards/<reward>",methods=["POST","GET"])
def admin_rewards(reward):
    
    return render_template("")

@app.route("/admin-products",methods=["POST","GET"])
def admin_products():
    if request.method == "POST":
        #Deletes Product from the product database
        with shelve.open("Databases/product") as f:
            #All button will have name="rm_product" and a value that corrosponds
            del f[request.form["rm_product"]] 
    #Admin can view all the products from the product database
    x = []
    with shelve.open("Databases/product") as f:
        for i in f:
            x.append(i)
    return render_template("", product=x)
        
@app.route("/admin-edit-info/<product>", methods=["POST","GET"])
def edit_product(product):
    #Updates product information
    if request.method == "POST":
        with shelve.open("Databases/product") as f:
            if request.form["name"] != None:
                f[product]["name"] = request.form["name"]
            if request.form["image"]!= None:
                f[product]["image"] = request.form["image"]
            if request.form["stocks"] != None:
                f[product]["stocks"] = request.form["stocks"]
            if request.form["desc"] != None:
                f[product]["desc"] = request.form["desc"]
            if request.form["points"] != None:
                f[product]["points"] = request.form["points"]
            if request.form["type"] != None:
                f[product]["type"] = request.form["type"]
            if request.form["categories"] != None:
                f[product]["categories"] = request.form["categories"]
            if request.form["RetailCost"] != None:
                f[product]["RetailCost"] = request.form["RetailCost"]
            if request.form["gender"] != None:
                f[product]["gender"] = request.form["gender"]
            if request.form["ListCost"] != None:
                f[product]["ListCost"] = request.form["ListCost"]
            if request.form["reviews"]!= None:
                f[product]["reviews"] = request.form["reviews"]

@app.route("/admin/userdata",methods=["POST","GET"])
def admin_user():
    if request.method == "POST":
        with shelve.open("Databases/user") as f:
            x = 0
            for i in f:
                if f[i]["name"] == request.form["Customer"]:
                    del f[i][str(x)]
                x += 1
    return render_template("admin_user")


@app.route("/admin/userdata/<user>", methods=["POST","GET"])
def admin_user_details(user):
    if request.method == "POST":
        with shelve.open("Databases/user") as f:
            x = 0
            for i in f:
                if f[i]["name"] == request.form["Customer"]:
                    if request.form["name" ] != None:
                        f[str(x)]["name"] ==  request.form["name"] 
                    if request.form["password" ] != None:
                        f[str(x)]["password"] ==  request.form["password"] 
                    if request.form["image" ] != None:
                        f[str(x)]["image"] ==  request.form["image"] 
                    if request.form["email" ] != None:
                        f[str(x)]["email"] ==  request.form["email"] 
                    if request.form["address" ] != None:
                        f[str(x)]["address"] ==  request.form["address"] 
                    if request.form["payment" ] != None:
                        f[str(x)]["payment"] ==  request.form["payment"] 
                    if request.form["point" ] != None:
                        f[str(x)]["point"] ==  request.form["point"] 
                    if request.form["cart" ] != None:
                        f[str(x)]["cart"] ==  request.form["cart"] 
                    x += 1
    return render_template("")

@app.route("/userdata/<user>",methods=["POST","GET"])
def user_details(user):
    if request.method == "POST":
        with shelve.open("Databases/user") as f:
            x = 0
            for i in f:
                if f[i]["name"] == request.form["Customer"]:
                    if request.form["name" ] != None:
                        f[str(x)]["name"] ==  request.form["name"] 
                    if request.form["password" ] != None:
                        f[str(x)]["password"] ==  request.form["password"] 
                    if request.form["image" ] != None:
                        f[str(x)]["image"] ==  request.form["image"] 
                    if request.form["email" ] != None:
                        f[str(x)]["email"] ==  request.form["email"] 
                    if request.form["address" ] != None:
                        f[str(x)]["address"] ==  request.form["address"] 
                    if request.form["payment" ] != None:
                        f[str(x)]["payment"] ==  request.form["payment"] 
                    if request.form["point" ] != None:
                        f[str(x)]["point"] ==  request.form["point"] 
                    if request.form["cart" ] != None:
                        f[str(x)]["cart"] ==  request.form["cart"] 
                    if request.form["role" ] != None:
                        f[str(x)]["role"] ==  request.form["role"] 
                    if request.form["del"] != None:
                        del f[str(x)]
                x+= 1
    return render_template("")


if __name__ == "__main__":
    initate()
    app.run(debug=True)
