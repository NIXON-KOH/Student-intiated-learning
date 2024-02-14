import shelve 
#DO NOT TOUCH THIS OR I WILL TOUCH YOU :D


f = shelve.open("Databases/user")
#id_, Role, name, JoinDate, Password, Image, Email
f["1"] = {"username":"nixon",
            "password":"1234",
            "JoinDate":"7-12-2023",
            "image" : "nixon.jpg",
            "role":"admin",
            "email":"233510P@mymail.nyp.edu.sg"}

#id_, Role, name, JoinDate, Password, Image, Email, Country, Address, PaymentMethod, Cart, History, Points
f["2"] = {"username":"kirsty",
            "password":"pass321",
            "role":"user",
            "image":"kirsty.jpg",
            "email":"232093z@mymail.nyp.edu.sg",
            "address":"nyp",
            "Paynow" : {"name":"No registered name","number":"No registered Account Number","cvv":"No registered cvv"},
            "Paypal" : {"email":"No Registered email","password":"No Registered password"},
            "JoinDate":"11-9-2001",
            "point":110,
            "cart":["kids_Checkers_Green_Coats"]}

f["3"] = {"username":"cayden",
            "password":"HelpMe9876",
            "role":"user",
            "image":"cayden.jpg",
            "email":"230340T@mymail.nyp.edu.sg",
            "address":"Changi",
            "History":{},
            "Paynow" : {"name":"No registered name","number":"No registered Account Number","cvv":"No registered cvv"},
            "Paypal" : {"email":"No Registered email","password":"No Registered password"},
            "JoinDate":"1-9-1939",
            "point":0,
            "cart":[]}

f["4"] = {"username":"gareth",
            "password":"password123",
            "role":"user",
            "image":"gareth.jpg",
            "email":"23456P@mymail.nyp.edu.sg",
            "address":"mhm",
            "History":{},
            "Paynow" : {"name":"No registered name","number":"No registered Account Number","cvv":"No registered cvv"},
            "Paypal" : {"email":"No Registered email","password":"No Registered password"},
            "JoinDate":"1-9-1939",
            "point":0,
            "cart":[]}

f["5"] = {"username":"irfun",
            "password":"Bala1",
            "role":"user",
            "image":"irfun.jpg",
            "email":"234637P@mymail.nyp.edu.sg",
            "address":"koko house",
            "History":{},
            "Paynow" : {"name":"No registered name","number":"No registered Account Number","cvv":"No registered cvv"},
            "Paypal" : {"email":"No Registered email","password":"No Registered password"},
            "JoinDate":"1-9-1939",
            "point":0,
            "cart":[]}
f.close()   

print("Success!!")