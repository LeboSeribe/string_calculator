#add function
# def add(*args):
    # counter = 0
    # for each_number in args:
            # counter += each_number
    # return counter


# print(add())  
# print(add(1)) 
# print(add(1,2))  
   

# string calculator

def add(string):
    my_sum = 0
    if string ==(''):
        return 0

    numbers = string.split(',')
    for each_number in numbers:
        number = float(each_number)
        my_sum += number
    return my_sum

print(add(''))
print(add('1'))
print(add('1,2'))
#all the first conditions passed

#supporting delimeters

