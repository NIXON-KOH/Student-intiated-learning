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
        query = request.form.get('chat')
        chatbot(query)
    
    return render_template("index.html")


@app.route("/rewards")
def rewards():
    return render_template("reward.html")

@app.route("/login",methods=["GET","POST"])
def authenticate():
    if request.method == "POST":
        username = request.form.get('name')
        password = request.form.get('password')
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

@app.route("/registration",methods=["GET",'POST'])
def registration():
    if request.method == "POST":
        username = request.form.get('name')
        password = request.form.get('password')
        email = request.form.get('email')
        address = request.form.get('address')

        with shelve.open('database') as f: 
            x = 1
            for i in f:
                if f[i]['username'] == username:
                    return redirect(url_for("register.html"))
                x += 1
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


@app.route("/shop")
def shop():
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


if __name__ == "__main__":
    initate()
    app.run(debug=True)