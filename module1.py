import random
def passcontrol(paswords):
    paswords=list(paswords)
def passauto()->str:
    """loob arvuti automatselt parool 
    """
    str0 = ".,:;!_*-+()/#¤%&"
    str1 = "123456789"
    str2 = "qwertyuiopasdfghjklzxcvbnm"
    str3 = str2.upper()
    print(str3) # 'QWERTYUIOPASDFGHJKLZXCVBNM'
    str4 = str0+str1+str2+str3
    print(str4)
    ls = list(str4)
    print(ls)
    random.shuffle(ls)
    print(ls)
    # Берём из списка 12 слюбых символов
    psword = ''.join([random.choice(ls) for x in range(12)])
    # Пароль готов 
    return psword
def paskontroll(psword:str)->bool:
    ls=list(psword)
    for e in ls:
        if e.isdigit(): d=True
        if e.isalpha(): a=True
        if e.isupper(): u=True
        if e.islower(): l=True
        if e in (".,:;!_*-+()/#%&"): s=True
    if d==True and a==True and u==True and l==True and s==True :
       t=True
    else:
        t=False
    return t 
def reg(users,passwords):
    while 1:
        log=input("kasutaja tunnus")
        if log not in users:
            print("Tunnus soobib")
            break
        else:
            print("see nimi juba on olemas listis")
    v=input("Arvuti-A või ise-I loob parool")
    if v.upper()=="A": 
        pas=passauto()
    elif v.upper()=="I":
        pas=input("Sisesta oma parool")
        tulemus=passcontrol(pas)
    if tulemus==True:
        user.append(log)
        passwords.append(pas)
def koik_kasutajad(users,passwords):
    """Вывод логина и пароля на экран
    """
    i=0
    for user in users:
        print(user, end="-")
        print(passwords[i])
        i+=1
def loe_failist_listisse(file:str)->list:
    """Loeme tekst failist ja salvesta järgemisse
    """
    f=open(file,"r")
    list_=[]
    for stroka in f:
        list_.append(stroka.strip())
    f.close()
    return list_
def faili_sisu_umberkirjutamine(file:str,list_:list):
    with open(file,"w") as f:
        for slovo in list:
            f.write(slovo+"\n")