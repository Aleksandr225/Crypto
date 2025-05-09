
import math

import random

alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ"
def hash(mes, p):
    h = 0
    for i in range(len(mes)):
        h = (h + (alphabet.index(mes[i])+1))**2 % p
    return h




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
    print(f"Число N: {N}")
    print(f"Число е: {e}")
    print(f"Число d: {d}")
    m = hash(string, P)
    print(f"Хеш: {m}")
    sig = m**d % N
    un_sig = sig**e%N

    print(f"Подпись: {sig}")
    
    print(f"Проверка подписи: {un_sig}")



def get_k(P, l):
    r = fi(P)
    while True:
        t = random.randint(1, r)
        if is_coprime(r, t) == True:
           return t


def el_sig():
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
        g = int(input("Введите число g "))
        if 1 < g < P:
            
            break
        else:
            print(f"1<g<{P}")

    while True:
        x = int(input("Введите число x "))
        
        if 1 < x < P:
            
            break
        else:
            print(f"1<x<{P}")
    

    y = g**x%P

    k = get_k(P, 1)
    

    print(f"Число Y: {y}")
    print(f"Число k: {k}")
    


    a = g**k%P

    print(f"Число a: {a}")


    m = hash(string, P)
    print(f"Число m: {m}")

    for i in range(P):
        if P-1 == m:
            if ((x*a + k*i) % (P-1)) == 0:
                b = i
                print(f"Число {b}")
                break
            
        if ((x*a + k*i) % (P-1)) == m:
            b = i
            print(f"Число {b}")
            break
    print(f"подпись {a, b}")
    

    a1 = (y**a)*(a**b) % P
    a2 = (g**m) % P

    print(f"Фрагмент А1: {a1}")
    print(f"Фрагмент А2: {a2}")
    




print("Выберите подпись:")
print("1 RSA")
print("2 EL Gamal")

ch = int(input())

if ch == 1:
    
    rsa()

elif ch == 2:
    el_sig()
    



