

def mod_exp(base, exp, mod): # Функция для быстрого возведения в степень по модулю
    result = 1
    while exp > 0:
        if exp % 2 == 1:  # если exp нечетное
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def dif_man():
    n = int(input("Введите общее число n: ")) 

    while True:
        a = int(input("Введите общее число a: "))
        if a > n:
            print("а должен быть меньше n")
            continue
        else:
            break

    while True:
        ka = int(input(f"Введите число Ka для первого пользователя(2, {n-1}): "))
        if  2 <= ka < n-1:
            break
        else:
            print(f"2 < ka < {n-1}")
            continue
    while True:
        kb = int(input(f"Введите число Kb для второго пользователя(2, {n-1}): "))
        if 2 <= kb < n-1:
            break
        else:
            print(f"2 < kb < {n-1}")
            continue
    
    
    Ya = a**ka % n
    Yb = a**kb % n

    print(f"Открытый ключ первого пользователя: {Ya}")
    print(f"Открытый ключ второго пользователя: {Yb}")

   
    secret_A = mod_exp(Yb, ka, n) 
    secret_B = mod_exp(Ya, kb, n)   

    if secret_A == 1 or secret_B == 1:
        print("В результате вышла единица, повторите алгоритм")
        dif_man()
    else:
        print(f"Секретный ключ ka: {secret_A}")
        print(f"Секретный ключ kb: {secret_B}")
    

dif_man()

#n = 41
#a = 7
#Ka = 6
#Kb = 10
