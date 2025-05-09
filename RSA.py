

import math
import random

alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ"


def is_prime(n):  
    if n <= 1:  
        return False  
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:  
            return False  
    return True  

def is_coprime(x, y):
    return math.gcd(x, y) == 1


def f_d(e, N):
    for i in range(N):
        if e*i % N == 1:
            return i
    


def fi(n):
    f = n
    if n%2 == 0:
        while n%2 == 0:
            n = n // 2
        f = f // 2
    i = 3
    while i*i <= n:
        if n%i == 0:
            while n%i == 0:
                n = n // i
            f = f // i
            f = f * (i-1)
        i = i + 2
    if n > 1:
        f = f // n
        f = f * (n-1)
    return f


def rsa():
    string = input("Введите сообщение: ")
    while True:
        while True:
            P = int(input("Введите число P (простое): "))
            if is_prime(P) == False:
                print("Число должно быть простым")
                continue
            else:
                break

        while True:
            Q = int(input("Введите число Q (простое): "))
            if is_prime(Q) == False:
                print("Число должно быть простым")
                continue
            else:
                break
        N = P*Q
        if N < 32:
            print("P*Q < 32")
            continue
        else:
            break
    f = fi((P)*(Q))
    
    while True:
        e = int(input(f"Введите е, 1 < e < {f} взаимноепростое с {f}: "))
        if is_coprime(f, e) == True:
            break
    d = f_d(e, f)
    print(d)
    fin = []
    for i in range(len(string)):
        ind = alphabet.index(string[i])
        temp = (ind**e) % N
        fin.append(temp)

    return fin


def rsaun(string):
    N = int(input("Введите число N: "))
    d = int(input("Введите d: "))
    tempt = []
    for i in range(len(string)):
        temp = (string[i]**d) % N
        tempt.append(temp)
    fin =[]
    for i in tempt:
        fin.append(alphabet[i])

    return(fin)



   
def get_k(P, l):
    r = fi(P)
    count = 0
    ks = []
    while count != l:
        t = random.randint(1, r)
        if is_coprime(r, t) == True:
            count +=1
            ks.append(t)
    return ks

def el_gamal():
    string = input("Введите сообщение: ")
    
    while True:
        P = int(input("Введите число P (простое): "))
        if is_prime(P) == False:
            print("Число должно быть простым")
            continue
        if P < 32:
            print("Число должно быть больше 32")
            continue
        else:
            break


    while True:
        x = int(input("Введите число x "))
        
        if 1 < x < P:
            
            break
        else:
            print(f"1<x<{P}")

    while True:
        g = int(input("Введите число g "))
        if 1 < g < P:
            
            break
        else:
            print(f"1<g<{P}")
 

    y = g**x%P

    print(f"Открытый ключ у: {y}")

    k = get_k(P, len(string))

    print(f"Рандомизаторы: {k}")
    
    fin=[]
    for i in range(len(string)):
        
        ind = alphabet.index(string[i])
        a = g**k[i]%P
        b = y**k[i]*ind%P
        fin.append([a,b])
    print(fin)
    return fin
    






def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def modular_inverse(a, p):
    gcd, x, _ = extended_gcd(a, p)
    if gcd != 1:
        raise ValueError(f"Обратного значения для {a} не существует по модулю {p}")
    else:
        return x % p

def solve_congruence(a, b, p):
    # Находим модульное обратное a по p
    a_inv = modular_inverse(a, p)
    # Находим x
    x = (a_inv * b) % p
    return x



#solution = solve_congruence(a, b, p)
    
def get_x(y,g,P):
    for i in range(P):
        if g**i%P ==y:
            return i
        


def el_gamalun(string):
    while True:
        P = int(input("Введите число P (простое): "))
        if is_prime(P) == False:
            print("Число должно быть простым")
            continue
        if P < 32:
            print("Число должно быть больше 32")
            continue
        else:
            break


    
    y = int(input("Введите число y: "))
        
        
    g = int(input("Введите число g "))
        

    x = get_x(y,g,P)

    fin = []
    for i in range(len(string)):
        a = string[i][0]**x
        b = string[i][1]
        l = solve_congruence(a, b, P)
        fin.append(l)
    fin2 =[]   
    for i in fin:
        fin2.append(alphabet[i])

    return fin2













############################################



print("Выберите шифр:")
print("1 RSA")
print("2 EL Gamal")
print("3 ECC")
ch = int(input())

if ch == 1:
    nn = rsa()
    print(f"Зашифрованное сообщение: {nn} ")
    un = rsaun(nn)
    print(f"Расшифрованное сообщение: {un} ")
elif ch == 2:
    el = el_gamal()
    print(f"Зашифрованное сообщение: {el} ")
    unel = el_gamalun(el)
    print(f"Расшифрованное сообщение: {unel} ")
