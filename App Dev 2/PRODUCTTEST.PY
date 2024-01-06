types = ["Shirt","Pants","Shoes"]
genders = ["Men","Women","Children","Infants"]
colors = ["Red", "Green", "Yellow", "Black", "white"]

products = []
for i in types:
    for ii in genders:
        for iii in colors:
            products.append(f"{ii}_{iii}_{i}")


import shelve
from tqdm import tqdm
import random

prices = [10,20,30,40,50]
cat = ["Sale", "New Arrival", "Out of Stock", "In Stock"]
for i in tqdm(range(60)):
    with shelve.open("Database/Products") as f:
        f[str(i)] = {
            "name" : str(products[i].replace("_"," ")),
            "pricing" : random.choice(prices),
            "categories" : random.choice(cat),
            "Gender" : products[i].split("_")[0],
            "color" : products[i].split("_")[1],
            "type" : products[i].split("_")[2],
            "rating" : random.randint(1,5),
            "image" : products[i] + ".jpg"
        }
