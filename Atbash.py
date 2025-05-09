
alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ"



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
    
    




def atbash():
    string = input("Введите сообщение: ")
    string = make_text(string, 1)
    n_string = []
    for i in range(len(string)):
        ind = alphabet.index(string[i]) #  
        indm = 32 - ind - 1
        n_string.append(alphabet[indm])
    print(arr_to_str(n_string))
    return n_string



def atbashun():
    string = input("Введите сообщение: ")
    string = make_text(string, 1)
    n_string = []
    for i in range(len(string)):
        ind = alphabet.index(string[i])
        indm =  -ind%32 -1
        n_string.append(alphabet[indm])
    t = make_text(arr_to_str(n_string), 2)
    print(t)
    return t


while True:
    print("Выберите режим расшифровки: \n 1. Зашифровать \n 2. расшифровать")
    ch = int(input("Ваш выбор: "))
    if ch == 1:
        atbash()

    if ch == 2:
        atbashun()

