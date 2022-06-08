# Homework
import sys

'''
1) Task - Главу прочитал полностью !
2) Task 2.. Example!
Я в этом примере сразу уместил все конструкции ! 
Тут я поработал с реальными файлами на компе + 3 файла не существует и обработал эту ошибку + 
еще информацию с 2 файлов разместил в списки ! 
1.urls_list = ['text1.txt', 'text2.txt', 'text3.txt']
urls_info = []
list_defect = []
for url in  urls_list:
    try:
        r = open(url)
        urls_info.append(r.read())
    except FileNotFoundError :
        list_defect.append(url)
    finally:
        m = open("full_urls.txt", 'a')
        for i in urls_info:
            m.write(i)
        m.write(str(list_defect))
        m.close()'''


''' Task 3
def some_function(arg1, arg2):
    try:
        return arg1 / arg2
    except ZeroDivisionError:
        return "ай яй яй делить на ноль можно не многим"
    except Exception as a:
        return a
    finally:
        print("I 'am happy that you learn python")


print(some_function(5, 0))'''
'''Task 4 
Тест я полностью прошел ! 
'''
'''Task 5 
На момент выполнения дз ! Итераторы мы уже прошли ) 

'''