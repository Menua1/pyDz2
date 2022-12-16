#Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для и получения случайного int
from random import randint

my_lst = ['31', '28', '30', '8', '13', '19']
nw_lst =[]
rnd = []
i = 0
while i < len(my_lst):
    random = randint(0, len(my_lst)-1)
    if random in rnd:
        continue
    else:
        nw_lst.append(my_lst[random])
        i +=1
        rnd.append(random)

print(*nw_lst,sep=',',end='.')