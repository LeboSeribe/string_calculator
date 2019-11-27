# string calculator
import re

def add(string):
    my_sum = 0
    x = re.compile(r"-?\d+?")

    
    numbers = x.findall(string)

    if string ==(''):
        return 0  

    for each_number in numbers:
        neg_list =[]
        number = int(each_number)
        if number < 0:
            neg_list.append(numbers)
            return neg_list
        if number>=0 :    
                my_sum += number
        # if :
            # return "it is anegative number"
    return my_sum
    # if each_number ==re.findall(r"[-]\d+"):
        # return "negative"
    


print(add(''))
# print(add('1,1'))
# print(add('1,2'))
# print(add('1\n2,3'))
# print(add('1,\n'))
# print(add('//;\n1;2'))
print(add('-5,-4'))
#all the first conditions passed

#supporting delimeters
# if there are negative numbers 
    # return (negative numbers with exception message)


