import requests
from bs4 import BeautifulSoup
import webbrowser
from collections import Counter

#FOR ASETHETICS LOL
from tqdm import tqdm
import os
import time

start = time.time()
os.system('cls' if os.name == 'nt' else 'clear')
#Getting the books
books = []
f = open("books.txt","r")
for x in f:
    x = x.replace("\n","")
    books.append(x)
f.close()
#Getting Book Genres
genres = []
rejected = []
b_id = 0
os.system('cls' if os.name == 'nt' else 'clear')
print("COLLECTING DATA ....")
for i in tqdm(range(len(books))):
    try:
        book = books[b_id]
        book = book.replace(" ","+")
        r = requests.get("https://www.goodreads.com/search?q="+book)
        soup = BeautifulSoup(r.content, 'html.parser')
        s = str(soup.find('a', class_='bookTitle'))
        s = s.split('"')
        web = s.index(' href=')
        web = s[web+1]
        r = requests.get("https://www.goodreads.com/"+web)
        soup = BeautifulSoup(r.content, 'html.parser')
        Genres = soup.find_all('span', {'class': 'Button__labelItem'})
        x = []
        
        for i in str(Genres).split('<span class="Button__labelItem">'):
            i = i.split("</span>,")
            i = i[0]
            x.append(str(i))

        n = x.index("...more")
        for i in range(1,8):
            genre = x[n-i]
            genres.append(genre)
    except:
        book = books[b_id]
        book = book
        rejected.append(book)

    b_id += 1
os.system('cls' if os.name == 'nt' else 'clear')
print("CLEANING DATA ....")
#Cleans up any errors in genres
n = -1

for w in tqdm(range(len(genres))):
    n += 1
    try:
        i = genres[n]
        
        if i.find("<") != -1:
        
            genres.pop(genres.index(i))

        elif ("Want to read" == i) or ("Jump to ratings and reviews" == i) or ("Buy on Amazon" == i) or ("Audiobook" == i):
            genres.pop(genres.index(i))
    except:
        pass
#Makes similar genres becomes the same
#Sorts and Counts each genre
Genre_count = {}
x = 0
Genre_count = Counter(genres)
genre_sort = dict(sorted(Genre_count.items(), key=lambda x: x[1],reverse=True))
#Getting book suggestions 
os.system('cls' if os.name == 'nt' else 'clear')
print("GETTING RECOMMENDATIONS.....")
x = 0
suggestion = []
genre_sort = list(genre_sort)
for i in tqdm(range(len(genre_sort))):
    query = ""
    for i in range(x):
        query += genre_sort[x]
    try:
        query = query.replace(" ","+")
    except:
        pass
    r = requests.get("https://www.goodreads.com/shelf/show/"+query)
    soup = BeautifulSoup(r.content, 'html.parser')
    n = str(soup.find_all('a', class_='bookTitle'))
    n = n.split('"')

    y = 4
    for i in range(round(len(n)/4)):

        title = n[y].split(">")[1]
        if ":" in title:
            title = title.split(":")[0]
        elif " (" in title:
            title = title.split(" (")[0]
        else:
            title = title

        link = "https://www.goodreads.com/"+ n[y-1]
        info = title + "|" + link
        y += 4
        suggestion.append(info)
    x += 1

#Refining The suggestions
os.system('cls' if os.name == 'nt' else 'clear')
print("REFINING SUGGESTIONS.....")
x = 0
file_to_delete = open("BOOKSUGGESTION.txt",'w')
file_to_delete.close()

for i in tqdm(range(len(suggestion))):
    s = suggestion[x].split("|")
    n = s[0].lower()
    present = "{0:50}  {1}".format(s[0],s[1])
    x += 1
    f = open("BOOKSUGGESTION.txt", "a")
    try : 
        f.write(present+"\n")
        f.close()
    except : 
        print(present)
path = os.path.abspath("BOOKSUGGESTION.txt")
webbrowser.open(path)
os.system('cls' if os.name == 'nt' else 'clear')
print("Rejected Data | ",len(rejected)," / " ,len(books))
print(rejected)
end = time.time()
print(f"Time taken: {(end-start)*10**3:.03f}ms")
print("-- COMPLETED --")
