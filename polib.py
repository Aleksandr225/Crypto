
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
    
    

polib = [['А','Б','В','Г','Д','Е'],
        ['Ж','З','И','Й','К','Л'],
        ['М','Н','О','П','Р','С'],
        ['Т','У','Ф','Х','Ц','Ч'],
        ['Ш','Щ','Ъ','Ы','Ь','Э'],
        ['Ю','Я']]

  


def polib_s():
    fin = []
    string = input("Введите сообщение: ")
    string = make_text(string,1)
    for k in range(len(string)):
        for i in range(6):
            for j in range(len(polib[i])):
                if polib[i][j] == string[k]:
                    
                    fin.append(str(i+1)+str(j+1))
                    break
    
    f = arr_to_str(fin)
    print(f)
    return fin

 
        



def polib_de(arr):
    
    fin = []
    for i in range(len(arr)):
        f_d = int(str(arr[i])[:1]) - 1
        s_d = int(str(arr[i])[1:]) - 1
        fin.append(polib[f_d][s_d])
    fin = arr_to_str(fin)
    fin  = make_text(fin, 2)
    print(fin)        

    
        
        



while True:
    print("Выберите режим расшифровки: \n 1. Зашифровать \n 2. расшифровать")
    ch = int(input("Ваш выбор: "))
    if ch == 1:
        n = polib_s()

    if ch == 2:
        polib_de(n)


