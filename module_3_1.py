calls = 0


def count_calls():
    global calls
    calls += 1
    return()


def string_info(str_):
    count_calls()
    str_lst = []
    str_lst.append(len(str_))
    str_lst.append(str_.upper())
    str_lst.append(str_.lower())
    str_tuple = tuple(str_lst)
    return(str_tuple)


def is_contains(st, ls):
    count_calls()
    for i in range(len(ls)):
        if st.casefold() == ls[i].casefold():
            return True
    else:

        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)