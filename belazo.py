
def arr_to_str(arr):
    string = ""
    for i in range(len(arr)):
        string += arr[i]    
    
    return string   



def make_text(text, r):
    if r == 1:
        reps = [(',', 'ЗПТ'), (' ', 'ПРБ'), ('.', "ТЧК"),("-", "ТТТ")]


        for char, rep in reps:
            if char in text:
                text = text.replace(char, rep)
        text = text.upper()
        return text
    
    if r == 2:
        reps = [('ЗПТ', ','), ('ПРБ', ' '), ('ТЧК', "."),("ТТТ", "-")]


        for char, rep in reps:
            if char in text:
                text = text.replace(char, rep)
        text = text.upper()
        return text
    
    





alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ"


def belazo():

    string = input("Введите сообщение: ")
    string = make_text(string,1)
    key = input("Введите ключ-слово: ")
    n_string = []
    k_index = 0
    for i in range(len(string)):
        n_letter =( alphabet.find(string[i]) + alphabet.find(key[k_index])) % len(alphabet)
        n_string.append(alphabet[n_letter])
        k_index+=1

        if k_index == len(key):
            k_index = 0
    print(arr_to_str(n_string))
    return n_string


def belazo_un():
    string = input("Введите сообщение: ")
    key = input("Введите ключ-слово: ")
    n_string = []
    k_index = 0
    for i in range(len(string)):
        n_letter =( alphabet.find(string[i]) - alphabet.find(key[k_index]))% len(alphabet)
        n_string.append(alphabet[n_letter])
        k_index+=1

        if k_index == len(key):
            k_index = 0
    print(make_text(arr_to_str(n_string),2))


while True:
    print("Выберите режим работы шифра белазо: \n 1. Зашифровать \n 2. расшифровать")
    ch = int(input("Ваш выбор: "))
    if ch == 1:
        n = belazo()

    if ch == 2:
        belazo_un()