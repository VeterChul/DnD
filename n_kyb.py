import re
import random as r
from all_text import start_mess, error_mess, list_help, ref, list_exa

list_mode = ["s", "b", "r"]

mode = 0

list_cub = []

list_com = ["ref", "ch_m", "cls", "help", "mode", "again",  "saved", "save", "", "throw"]
list_def = {
    'ch_m' : (lambda mas : print(list_mode[mode])),
    'cls' :  (lambda mas : print("\n"*50)), 
    'help' : (lambda mas : print_help(mas)),
    'ref' :  (lambda mas : print_ref()),
    'mode' : (lambda mas : svipe_mode(mas)),
    'again' : (lambda mas : throw_again(mas)),
    'saved' : (lambda mas : print_saved(mas)),
    'save' : (lambda mas : new_cub(mas)),
    '' : (lambda mas : __again(mas)),
    'throw' : (lambda mas : throw(mas)),
    }

old_s = (0, 0)

def test_kyb(k,ch = 1):
    return ch <= 40 and k <= 150 and ch > 0 and k > 0

def mass(n):
    m = []
    for i in range(n):
        for j in range(i*i):
            m.append(i+1)
    return r.choice(m)

def kyb(k, ch = 1, chit = False):
    global old_s
    if not(k in [4, 6, 8, 10, 12, 20, 100, 3, 5]):
        print("Вы ввели куб не состоящий в стандартном наборе D&D. Проверте правильность ввода.", end="\n")
    for i in range(ch):
            if chit:
                n = mass(k)
            else:
                n = r.randint(1, k)
            if k == 100:
                    n -= 1        
            print(f"С куба k{k} выпало:", n) 
            old_s = (ch, k)
    return 0

def svipe_mode(mas):#сменить мод
    global mode, list_mode, error_mess
    try:
        if len(mas) == 1:
            mode = 0
            return 0
        mode = list_mode.index(mas[0])
        print(f"Мод сменён на {list_mode[mode]}")
    except:
        print(error_mess, "Ошибка изменения мода. Проверьте првильность ввода.\nНапишите ref для получения справки.")

def print_saved(mas):#Вывод сохраненных кубов
    global list_cub
    try:
        if len(mas) == 1:
            mas = [1, len(list_cub)]
        if mas[0] < 1:
            mas[0] = 1
        if mas[1] > len(list_cub):
            mas[1] = len(list_cub)
        print("У вас есть сохранёные кубы:")
        for i in range(int(mas[0]) - 1, int(mas[1])):
            print(f"    {i + 1} : {list_cub[i][0]}k{list_cub[i][1]}")
    except:
        print(error_mess, "Ошибка вывода кубов. Проверьте првильность ввода.\nНапишите ref для получения справки.")

def new_cub(mas):#создать новый куб
    global list_cub
    try:
        if re.search("[0-9]*[dkк][0-9]+", mas[0]):
            list_cub.append(open_ky(mas[0]))
            print(f"Записан новый куб под номером {len(list_cub)}. Значение {list_cub[-1][0]}k{list_cub[-1][1]}")
            return 0
        if int(mas[0]) - 1 < len(list_cub):
            list_cub[int(mas[0]) - 1] = open_ky(mas[1])
            print(f"Куб номер {mas[0]} перезаписан. Новое значение {list_cub[int(mas[0]) - 1][0]}k{list_cub[int(mas[0]) - 1][1]}")
        else:
            list_cub.append(open_ky(mas[1]))
            print(f"Записан новый куб под номером {len(list_cub)}. Значение {list_cub[-1][0]}k{list_cub[-1][1]}")
    except:
        print(error_mess, "Ошибка при создании куба. Проверьте првильность ввода.\nНапишите ref для получения справки.")

def __again(mas):#ентер
    global mode, old_s
    if mode == 0:
        kyb(20, 1, mas[-1])
    else:
        kyb(old_s[1], old_s[0], mas[-1])

def throw(mas):#кинуть сохраненый куб
    try:
        global mode, list_cub, old_s
        kybb = list_cub[int(mas[0]) - 1]
        kyb(kybb[1], kybb[0], mas[-1])
    except:
        print(error_mess, "Ошибка при броске сохраненного куба. Проверьте првильность ввода.\nНапишите ref для получения справки.")

def throw_again(mas):#перекинуть последний куб
    try:
        global old_s
        if old_s[0] == 0:
            print("Вы ещё не кидали кубов")
            return 0
        kyb(old_s[1], old_s[0], mas[-1])
    except:
        print(error_mess, "Ошибка при броске прошлого куба. Проверьте првильность ввода.\nНапишите ref для получения справки.")

def print_help(mas):#Вывод help
    try:
        global list_mode, mode, list_help
        if len(mas) == 1:
            h = f"Вы находитесь в режиме {list_mode[mode]}.\nДля получения справки пропишите 'ref'"
            print(h)
            return 0
        else:
            print(f"{mas[0]} - {list_help[mas[0]]}.\nПример:\n{list_exa[mas[0]]}")
            return 0
    except:
        print(error_mess, "Ошибка при выводе help. Проверьте првильность ввода.\nНапишите ref для получения справки.")

def print_ref():#Вывод справки
    global list_mode, mode, ref
    print(ref)
    return 0

def open_ky(ky):
    try:
        if "k" in ky:
            m = ky.split("k")
        if "d" in ky:
            m = ky.split("d")
        if "к" in ky:
            m = ky.split("к")
        return [int(m[0]), int(m[1])]
    except:
        print(error_mess, "Ошибка при разделение кубов. Проверьте првильность ввода.\nНапишите ref для получения справки.")

print(start_mess)

s = input()

while s != 'q':
    try:
        if s != "":
            chit = s[0] == " "
            s = s.split()
            s.append(chit)
        else:
            chit = False
            s = ["", chit]
        if s[0] in list_com:
                list_def[s[0]](s[1:])
        else:    
            if mode in (0, 2):
                if len(s) == 2:
                    kyb(int(s[0]), chit = chit)
                else:
                    kyb(int(s[1]), int(s[0]), chit = chit)
            elif mode in (1, ):
                throw([s[0], chit])
    except:
        print(error_mess,"Ошибка не известна, код 1") 
    finally:
        s = input()

print("Спасибо, что воспользовались программой. Желаем ещё собраться за столом")
