def search(value, my_list):
    """Returns the index of a requested value"""
    index = 0
    # print(my_list)
    for i in my_list:
        if i == value:
            return index
        else:
            index += 1
    return None


def count(value, my_list):
    """Returns the number of times a requested value is in the list"""
    my_list.sort()
    counter = 0
    # print(my_list)
    for i in my_list:
        if i == value:
            counter += 1
    return counter


def binary_find(value, my_list):
    """Sorts the list and returns the index of the requested value"""
    my_list.sort()
    print(my_list)
    found = False
    first = 0
    last = len(my_list) - 1
    while first <= last and not found:
        mid = (first + last) // 2
        if value < my_list[mid]:
            last = mid - 1
        elif value > my_list[mid]:
            first = mid + 1
        else:
            found = True

    if not found:
        mid = None

    return mid


def main1():
    print('MAIN 1: Sequential')
    a = [5, 332, 6, 8, 91, 123, 123, 3]
    valid = False
    while not valid:
        selection = input('Please type an integer to search in the list: ')
        try:
            selection = int(selection)
            valid = True
        except ValueError:
            print('Incorrect input type. Please try again.\n')

    location = search(value=selection, my_list=a)
    if location == None:
        print('Value of {} not found.\n'.format(str(selection)))
    else:
        print('Index: ' + str(location))
        print('Value at index {}: {}\n'.format(str(location), str(a[location])))


def main2():
    print('MAIN 2: Smart sequential')
    a = [5, 332, 6, 8, 91, 123, 91, 91, 123, 3]
    valid = False
    while not valid:
        selection = input('Please type an integer to search in the list: ')
        try:
            selection = int(selection)
            valid = True
        except ValueError:
            print('Incorrect input type. Please try again.\n')

    num = count(value=selection, my_list=a)
    print('Value {} has been found {} times.\n'.format(str(selection), str(num)))


def main3():
    print('MAIN 3: Binary search')
    a = [5, 332, 6, 8, 91, 123, 91, 91, 123, 3]
    valid = False
    while not valid:
        selection = input('Please type an integer to search in the list: ')
        try:
            selection = int(selection)
            valid = True
        except ValueError:
            print('Incorrect input type. Please try again.\n')

    look_for = binary_find(value=selection, my_list=a)
    if look_for is None:
        print('Value {} has not been found.\n'.format(str(selection)))
    else:
        print('Value {} has been found at index {}.\n'.format(str(selection), str(look_for)))


main1()
main2()
main3()