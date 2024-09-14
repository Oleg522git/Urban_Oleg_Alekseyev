#from idlelib.configdialog import is_int
from idlelib.configdialog import is_int

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, '11' , 13 , 'hg']
primes = []
not_primes = []
not_int = []
is_prime = True

for i in range(len(numbers)):
    if numbers[i] == 1 or numbers[i] == 0 or isinstance(numbers[i], int) != True:
        if isinstance(numbers[i], int) != True:
            not_int.append(numbers[i])
        continue
    else:
        for j in range(i+1):
#            print(numbers[j] , 'is' , type(numbers[j]))
            if numbers[j] == 1 or numbers[j] == 0 or numbers[i] == numbers[j] or isinstance(numbers[j], int) != True:
                continue
            else:
                ni_nj = numbers[i] % numbers[j]
                is_prime = bool(is_prime * ni_nj)
    if (is_prime == True):
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])
    is_prime = True

print('исходный список' , numbers)
print('простые числа', primes)
print('не простые (составные) числа ', not_primes)
print('не числа', not_int)