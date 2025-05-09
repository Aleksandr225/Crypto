

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



def shizar():
    string = input("Введите сообщение: ")
    string = make_text(string,1)
    while True:
        dig = int(input("Введите ключ: "))
        if dig < 1 or dig >31:
            print("Неверный ключ")
            continue
        else:
            break

    n_string = []
    for i in range(len(string)):
       index = (alphabet.find(string[i]) + dig) % 32
       n_string.append(alphabet[index])
    print(arr_to_str(n_string))

    return n_string





def shizar_en():
    string = input("Введите сообщение: ")
    
    while True:
        dig = int(input("Введите ключ: "))
        if dig < 1 or dig >31:
            continue
        else:
            break
    n_string = []
    for i in range(len(string)):
       index = (alphabet.find(string[i]) - dig) % 32
       n_string.append(alphabet[index])
    nn = arr_to_str(n_string)
    n = make_text(nn, 2)
    print(n)

    return(n_string)





while True:
    print("Выберите режим расшифровки: \n 1. Зашифровать \n 2. расшифровать")
    ch = int(input("Ваш выбор: "))
    if ch == 1:
        shizar()

    if ch == 2:
        shizar_en()