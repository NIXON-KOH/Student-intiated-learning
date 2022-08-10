import os
import time
import networkx as nx
import matplotlib.pyplot as plt
import instaloader
clear = lambda:os.system('cls')
clear()

start_time = time.time()
name = input("Instagram account \n> ")
open('friend.txt', 'w').close()

L = instaloader.Instaloader()
L.login("theriseof_x","123412341234")
profile = instaloader.Profile.from_username(L.context, name)

followers = []
count = 0
for followers1 in profile.get_followers():
    followers.append(followers1.username)
    print(followers[count])
    count += 1

following = []
count = 0
for followees1 in profile.get_followees():
    following.append(followees1.username)
    print(following[count])
    count += 1

Friend = set(followers) & set(following)

for i in Friend:
    for f in followers:
        if i == f:
            followers.remove(i)

for i in Friend:
    for f in following:
        if i == f:
            following.remove(f)


for i in Friend:
    file = open("friend.txt","a+")
    file.write(f"Friend {i}")
    file.write("\n")
    file.close()

for i in following:
    file = open("friend.txt","a+")
    file.write(f"following {i}")
    file.write("\n")
    file.close()
    
for i in followers:
    file = open("friend.txt","a+")
    file.write(f"followers {i}")
    file.write("\n")
    file.close()

G = nx.read_edgelist("friend.txt", create_using = nx.Graph(), nodetype=str)
'''friend list should be {relation name} Value for relations will be
Friend, Following,Followed'''

options = {
    "width": 0.1,
    "with_labels": True,
    "node_color" : "white",
}
nx.draw_networkx(G,**options)
ax = plt.gca()
ax.margins(x = 0.01)
plt.axis("off")
print(f"Runtime: {time.time() - start_time}")
plt.show()


