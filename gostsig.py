
import math



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

def get_a(P, Q):
    arr = []
    for i in range(P):
        if i**Q%P == 1 and i < P-1:
            arr.append(i)
    return arr


def get_q(P):
    qarr = []
    for i in range(1,P):
        if ((P-1) % i == 0) and (is_prime(i) == True):
            qarr.append(i)

    return qarr




def gost():
    string = input("Введите сообщение: ")
    while True:
        P = int(input("Введите число P (простое): "))
        if is_prime(P) == False:
            print("Число должно быть простым")
            continue
        else:
            break

    while True:
        qarr = get_q(P)
        print(f"Возможные значения Q: {qarr}")
        Q = int(input("Введите число Q (простое): "))
        if is_prime(Q) == False or (P-1)% Q != 0:
            print("Число должно быть простым и быть делителем для P-1")
            continue
        else:
            break

    while True:
        arr = get_a(P,Q)
        print(f"Возможные значения а: {arr}")
        a = int(input("Введите число a: "))
        if (a > P-1) or (a**Q)%P != 1:
            print(f"Число должно быть меньше {P-1} и a**Q%P == 1")
            continue
        else:
            break

    while True:
        x = int(input("Введите число x: "))
        if x > Q:
            print(f"Число должно быть меньше {Q}")
            continue
        else:
            break

    while True:
        k = int(input("Введите число k: "))
        if x > P:
            print(f"Число должно быть меньше {P}")
            continue
        else:
            break
    




    y = a**x%P
    
    m = hash(string, P)
    r = (a**k % P) % Q
    s = (x*r+k*m) % Q

    print(f"Число y: {y}")
    print(f"Число k: {k}")
    print(f"Число m: {m}")
    print(f"подпись r, s: {r, s}")
    

    v = m**(Q-2)
    z1 = (s*v) % Q
    z2 = ((Q-r)*v) % Q
    u = (((a**z1*y**z2)% P) % Q)


    print(f"Число v: {v}")
    print(f"Число z1: {z1}")
    print(f"Число z2: {z2}")


    print(f"Число r: {r} Число u: {u}")

gost()