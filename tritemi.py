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




def tritemi():
    string = input("Введите сообщение: ")
    string = make_text(string,1)
    n_string=[]
    index = 0
    for i in range(len(string)):
        al_in = alphabet.find(string[i])
        ind = (al_in+index) % len(alphabet) 
        n_string.append(alphabet[ind])
        index +=1
        if index == 32:
            index = 0
    print(arr_to_str(n_string))
    return n_string

def tritemi_un():
    string = input("Введите сообщение: ")
    n_string=[]
    index = 0
    for i in range(len(string)):
        al_in = alphabet.find(string[i])
        ind = (al_in-index) % len(alphabet) 
        n_string.append(alphabet[ind])
        index +=1
        if index == 32:
            index = 0
    print(make_text(arr_to_str(n_string),2))
    return n_string




while True:
    print("Выберите режим расшифровки: \n 1. Зашифровать \n 2. расшифровать")
    ch = int(input("Ваш выбор: "))
    if ch == 1:
        n = tritemi()

    if ch == 2:
        tritemi_un()