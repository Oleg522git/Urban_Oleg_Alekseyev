my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
l = len(my_list)

#Решение 1
i = 0
while i < l:
    if my_list[i] == 0:
         i += 1
         continue
    elif my_list[i] > 0:
        print(my_list[i])
        i += 1
    else:
        break
print('The end 1')

#Решение 2
i = 0
while i < l:
    if my_list[i] != 0:
        if my_list[i] > 0:
            print(my_list[i])
        else:
            break
        i += 1
        continue
    i += 1
print('The end 2')

#Решение 3
i = -1
while i < l:
    i += 1
    if my_list[i] != 0:
        if my_list[i] > 0:
            print(my_list[i])
        else:
            break
        continue
print('The end 3')