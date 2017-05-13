'''
Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) 
and another number. The function decides whether or not the given number is inside the list and returns 
(then prints) an appropriate boolean.
Extras: Use binary search.
'''

import random

def _create_random_list_():
    #create random list with large number of items
    lstRandom = []
    for x in range (0,100):
        lstRandom.append(random.randint(0,100))
    return lstRandom

def _arrangeList_(lstGlobal):
    # arrange list and remove dublicates
    lstOrder = []
    ind1 = 0
    while ind1 < 100:
        for i in lstGlobal:
            if i == ind1 and ind1 not in lstOrder:
                lstOrder.append(ind1)
        ind1 += 1
    return lstOrder

'''
def _compare_number_to_list_(iNumber, lstGlobal):
    #take number and see if it is in a list
    if iNumber in lstGlobal:
        return True
    else:
        return False
'''


def _compare_number_to_list_(iNumber, lstGlobal):
    start_index = 0
    end_index = len(lstGlobal) - 1

    while True:
        middle_index = int((end_index + start_index) / 2)

        #last possible???
        if middle_index == start_index or middle_index == end_index:
            if lstGlobal[middle_index] == iNumber or lstGlobal[end_index] == iNumber:
                return True
            else:
                return False
        
        #first tried
        middle_element = lstGlobal[middle_index]
        if middle_element == iNumber:
            return True
        #iterate
        elif middle_element < iNumber:
            end_index = middle_index
        else:
            start_index = middle_index

lstGlobal = _create_random_list_()
#print('RandomList: ', lstGlobal)

lstGlobal = _arrangeList_(lstGlobal)
#print('ListOrder: ', lstGlobal)

iNumber = int(input('Give me a number 0-100. And see if it in randomly created pool of 100 samples: '))
print(_compare_number_to_list_(iNumber, lstGlobal))

#print(_compare_number_to_list_(iNumber,_arrangeList_(_create_random_list_())))
