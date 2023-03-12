import sys 
import time
import os 
from tqdm import tqdm


def delay_print(x):
    for l in x:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.05)

def error():
    delay_print("--Error--\nENIGMA HAS ENDED")
    sys.exit()


def settings():

    rotor = input("Rotor serial\n> ")
    if len(rotor) != 3:
        error()

    rotor_setting = input("Rotor Settings (01 02 03)\n> ")
    rotor_settings1 = rotor_setting.split(" ")
    rotor_settings = []

    for i in rotor_settings1:
        try:
            x = int(i)
        except:
            error()
        if type(x) is int:
            rotor_settings.append(i)
        else:
            error()

    if len(rotor_settings) != 3:
        error()
    else:
        pass

    plug = input("Plug Settings (AB CD ...)\n> ")
    plugs = (plug.upper()).split(" ")
    plugged = []

    for i in plugs:
        if len(i) == 2:
            plugged.append(i)
        elif len(i) == 0:
            pass
        else:
            error()
    
    os.system('cls' if os.name == 'nt' else 'clear')
    delay_print("Rotor Serial > " + rotor + "\n")
    delay_print("Rotor Settings > " + rotor_setting + "\n")
    delay_print("Plug > " + plug + "\n" )
    message = (input("Messages \n> ")).upper()
    return rotor,rotor_settings,plugged,message



def encryption(rotor,rotor_settings,plug,message):
    Done = []
    letters = ['.','0','1','2','3','4','5','6','7','8','9','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',' ']


    rotor_1 = [22, 1, 6, 17, 7, 2, 13, 21, 28, 24, 34, 3, 14, 36, 9, 29, 15, 23,37, 31, 18, 0, 10, 20, 27, 11, 25, 33, 5, 8, 19, 30, 12, 35, 26, 16, 4, 32]
    rotor_2 = [25, 1, 16, 21, 6, 5, 19, 9, 12, 23, 15, 18, 8, 0, 26, 2, 36, 30, 31,37, 29, 22, 27, 3, 35, 20, 33, 13, 10, 32, 4, 17, 14, 11, 7, 28, 24, 34]
    rotor_3 = [34, 8, 21, 11, 18, 9, 26, 28, 7, 1, 3, 22, 30, 2, 16, 12, 5, 17, 6, 19,37, 10, 0, 27, 23, 29, 31, 14, 13, 25, 20, 35, 33, 24, 32, 4, 15, 36]
    rotor_4 = [26, 16, 19, 0, 17, 5, 22, 13, 30, 3, 24, 7, 29, 10, 9, 32, 11, 33, 8, 23, 37,12, 27, 18, 15, 20, 34, 6, 36, 4, 35, 31, 2, 21, 14, 28, 1, 25]
    rotor_5 = [20, 25, 19, 35, 36, 22, 33, 16, 1, 30, 13, 18, 2, 24, 29, 10, 0, 4, 32, 12,37, 6, 31, 5, 9, 7, 11, 8, 21, 28, 3, 23, 26, 15, 34, 14, 27, 17]
    rotor_6 = [11, 2, 20, 33, 29, 12, 27, 10, 16, 25, 26, 18, 19, 0, 14, 7, 22, 36, 3, 34, 21,37, 17, 15, 32, 9, 1, 35, 28, 6, 30, 23, 31, 5, 4, 13, 24, 8]
    deflector = [21, 35, 29, 13, 1, 25, 11, 27, 24, 2, 22, 9, 7, 33, 12, 5, 18, 32, 10, 30, 31, 16,37, 28, 14, 20, 15, 19, 8, 6, 23, 36, 0, 3, 34, 4, 26, 17]
    rotors = []
    #setting up the rotor
    for a in rotor:
        if a == "a":
            rotors.append(rotor_1)
        elif a == "b":
            rotors.append(rotor_2)
        elif a == "c":
            rotors.append(rotor_3)
        elif a == "d":
            rotors.append(rotor_4)
        elif a == "e":
            rotors.append(rotor_5)
        elif a == "f":
            rotors.append(rotor_6)
    x = 0
    rotor_changed = []
    #setting according to rotor settings
    for i in rotor_settings:

        i = int(i)
        z = rotors[x]
        a = z[i:]
        b = z[:i]
        c = a + b
        rotor_changed.append(c)
        x += 1

    x = 0
    y = 0
    z = int(len(message))
    deflector_dict = {
    "0": 17,
    "1": 20,
    "2": 36,
    "3": 31,
    "4": 10,
    "5": 16,
    "6": 27,
    "7": 33,
    "8": 26,
    "9": 21,
    "10": 4,
    "11": 25,
    "12": 35,
    "13": 23,
    "14": 22,
    "15": 32,
    "16": 5,
    "17": 0,
    "18": 29,
    "19": 34,
    "20": 1,
    "21": 9,
    "22": 14,
    "23": 13,
    "24": 30,
    "25": 11,
    "26": 8,
    "27": 6,
    "28": 37,
    "29": 18,
    "30": 24,
    "31": 3,
    "32": 15,
    "33": 7,
    "34": 19,
    "35": 12,
    "36": 2,
    "37": 28
    }
    
    for n in tqdm(range(len(message))):
        char = message[n]


        #plug board
        for n in plug:
            if n[0] == char:
                char == n[1]
            elif n[1] == char:
                char == n[0]
            else:
                pass
        #Happens every letter
        if x != 0:
            z = rotor_changed[0]    
            rotor_changed[0] = z[1:] + [z[0]]
        else:
            pass
        #rotor 1 finishes oscilliation
        if x >= 37:
            z = rotor_changed[1] 
            rotor_changed[1] = z[1:] + [z[0]]
            x = 0
        else:
            pass
        #rotor 2 finishes oscilliation
        if y == 37:
            z = rotor_changed[2]    
            rotor_changed[2] = z[1:] + [z[0]]
            y = 0
        else:
            pass

        b = letters.index(char)
        for i in rotor_changed:
            pass 
            b = i[b]
            

        d_in = deflector[(b)]
        d_out = deflector_dict[str(d_in)]
        
        b = deflector.index(d_out)

        a = len(rotor_changed) - 1 
        for i in rotor_changed:
            b = i[a].index(b)
            a -= 1    
        

        character = str(letters[b])
        a = 0
        #plug board
        for n in plug:
            if str(plug[a][1]) == str(character):
                character = str(plug[0])
            elif str(plug[a][0]) == str(character):
                character = str(plug[1])
            else:
                pass
        Done.append(character)
        x += 1
        time.sleep(0.05)
    
    Dones = ''.join(Done)
    return Dones


if __name__ =="__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    rotor,rotor_settings,plug,message = settings()
    Done = encryption(rotor,rotor_settings,plug,message)
    delay_print(Done)
    print("---")


