import random
import time
import subprocess

##install keyboard##
try:
    import keyboard
except ModuleNotFoundError:
    subprocess.call("pip3 install keyboard")
finally:
    print("Module installed")

def fwrite(name, text):
    with open(name, "a+") as foo:
        for line in text:
            foo.write(line[0])

def fread(name):
    with open(name, "r") as foo:
        data = foo.readlines()
        ret = []
        for line in data:
            ret.append([line])
        return ret

broken = False
while True:
    name = input ("Enter Username: ")
    userfound = False
    pwordcorr = False
    new = []
    for line in fread("piGameInfo.txt"):
        new.append(line[0].split(","))
    for acc in new:
        if name == acc[0]:
            userfound = True
            pwd= input ("Enter Password: ")
            if pwd == acc[1].strip():
                pwordcorr = True
                print ("Welcome")
                broken = True
    if broken:
        break
    if not pwordcorr and userfound:  
        print ("Incorrect login, check details and try again")
        acc = input("Create new account? ").lower()
        if acc == "y" or acc == "yes":
            adminpass = input("Enter the admin password to create a new account: ")
            if adminpass == "admin":
                nwnm = input ("Enter new username: ")
                newpass = input ("Enter new password: ")
                break
    elif not userfound:
        print("Incorrect Username")
        acc = input("Create new account? ").lower()
        if acc == "y" or acc == "yes":
            adminpass = input("Enter the admin password to create a new account: ")
            if adminpass == "admin":
                nwnm = input ("Enter new username: ")
                newpass = input ("Enter new password: ")
                break
            
if pwordcorr and userfound:
    new = []
    for line in fread("piGameInfo.txt"):
        new.append(line[0].split(","))
    for acc in new:
        score = int(acc[2].strip())
else:
    score = 0


k = True
while k:
    game = True
    digit = 0
    pi = str("3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989")
    play=input("Would you like to play?: ")
    if play == "yes" or play == "y" or play == "Yes" or play == "Y":
        print("Okey dokey!")
        print("When Incorrect appears press enter")
        print("Begin typing pi: ")
        while game == True:
            try:
                if keyboard.read_key() == (pi[digit]):
                    digit = digit + 1
                    game = True
                elif keyboard.read_key() != (pi[digit]):
                    game = False
                    input("Incorrect\n")
                    print("Congratulations! You know pi to", (digit - 2), "decimal places!")
                    print("Pi to", (digit - 1), "decimal places is:", (pi[0:digit+1]))
                    cont=input("Would you like to play again?")
                    if cont == "yes" or cont == "y" or cont == "Yes" or cont == "Y":
                        print("Okey dokey!")
                        if digit - 2 > score:
                            score = digit -2
                        k = True
                    else:
                        print("No? Okay.")
                        k = False
                        if digit - 2 > score:
                            score = digit - 2
                        break
            except:
                break
    else:
        print("No? Okay.")
        k = False
        if digit - 2 > score:
            score = digit - 2

time.sleep(1)
print ("Your best score is:",score)
       
if pwordcorr and userfound:
    fwrite("piGameInfo.txt", [[name+","+pwd+","+str(score)+"\n"]])
else:
    fwrite("piGameInfo.txt", [[nwnm+","+newpass+","+str(score)+"\n"]])
