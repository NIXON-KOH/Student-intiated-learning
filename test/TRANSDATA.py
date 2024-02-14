import shelve
import datetime
with shelve.open("Databases/transaction") as f:
    f[str(1)] = {
        "id" : 1,
        "Date" : str(datetime.date.today()),
        "Product" : "kids_Checkers_Green_Coats",
        "Cust" : "kirsty",
        "Status" : "Delivered",
        "Price" : "10.99"
    }
    f[str(2)] = {
        "id" : 2,
        "Date" : str(datetime.date.today()),
        "Product" : "kids_Checkers_Green_tracksuit",
        "Cust" : "cayden",
        "Status" : "active",
        "Price" : "10.99"
    }
    f[str(3)] = {
        "id" : 3,
        "Date" : str(datetime.date.today()),
        "Product" : "kids_Checkers_Green_tracksuit",
        "Cust" : "cayden",
        "Status" : "active",
        "Price" : "10.99"
    }

