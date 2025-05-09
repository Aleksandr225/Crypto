import math


def is_coprime(x, y):
    return math.gcd(x, y) == 1

phrase = "КРАСИВЫМИСЛОВАМИПАСТЕРНАКНЕПОМАСЛИШЬТЧК"
alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ"

def shenon():
    string = input()
    m = 32
    shen = []
    a = 0
    while a % 2 ==0 or a > 32 or a == 0 and a%4 ==1:
        print("Введите число а")
        a = int(input())
        if (a % 2  == 0 ) or a > 32:
            print("a - Должно быть нечетным числом0")

    while True:
        print("Введите число c")
        c = int(input())
        test = is_coprime(c, m)
        if test == True and c < 32 and c != 0:
            break
        else:
            print("Число с должно быть взаимнопростым с модулем m")
    


    print("Введите число T")
    t = int(input())

    shen.append((a*t+c)%m)

    for i in range(len(string)-1):
        temp = (a*shen[i]+c)%32
        shen.append(temp)

    n_string = []

    for i in range(len(string)):
        b = (alphabet.find(string[i]) + shen[i]) % m
        n_string.append(b)

    print(n_string)
    return n_string


        
    

nn = shenon()


def shen_un(string):
    
    m = 32
    shen = []
    a = 0
    while a % 2 ==0:
        print("Введите число а")
        a = int(input())
        if a % 2 == 0:
            print("a - Должно быть нечетным числом")

    while True:
        print("Введите число c")
        c = int(input())
        test = is_coprime(c, m)
        if test == True:
            break
        else:
            print("Число с должно быть взаимнопростым с модулем m")
    


    print("Введите число T")
    t = int(input())

    shen.append((a*t+c)%m)

    for i in range(len(string)-1):
        temp = (a*shen[i]+c)%32
        shen.append(temp)

    n_string = []

    for i in range(len(string)):
        b = ((string[i]) - shen[i]) % m
        n_string.append(b)

    fin_string = []
    for i in range(len(n_string)):
        fin_string.append((alphabet[n_string[i]]))
    print(fin_string)


shen_un(nn)
