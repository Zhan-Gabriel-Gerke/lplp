from module1 import *
users=["Zan"]
passwords=["12345"]

while True:
    print("Näita kõike -0,Reg-1,Avt-2,Välja-3")
    v=int(input())
    if v==0:
        koik_kasutajad(users,passwords)  
    if v==1:
        print("Registreriumine")
        reg()
    elif v==2:
        print("Avtoriseriumine")
        log=input("Login:")
        if log not in users:
            print("sinu ei rigiistrirtud")
        pas=input("Paswoerd:")
        if pas not in password:
            print("viga")
    elif v==3:
        print("Välja")
        #
        break
    else:
        print("On vaja valida 1,2 või 3")