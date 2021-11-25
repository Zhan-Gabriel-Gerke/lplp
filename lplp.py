from module1 import *
users=loe_failist_listisse("Textfile2.txt")
passwords=loe_failist_listisse("TextFile3.txt")

while True:
    print("Näita kõike -0,Reg-1,Avt-2,Välja-3")
    v=int(input())
    if v==0:
        koik_kasutajad(users,passwords)  
    elif v==1:
        print("Registreriumine")
        reg(users,passwords)
        t=passcontrol(passwords)
    elif v==2:
        print("Avtoriseriumine")
        log=input("Login:")
        if log not in users:
            print("sinu ei rigiistrirtud")
        pas=input("Paswoerd:")
        if pas not in passwords:
            print("viga")
    elif v==3:
        print("Välja")
        faili_sisu_umberkirjutamine("Textfile2.txt")
        faili_sisu_umberkirjutamine("Textfile3.txt")
        break
    else:
        print("On vaja valida 1,2 või 3")