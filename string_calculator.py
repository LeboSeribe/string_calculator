# string calculator
import re

def add(string):
    my_sum = 0
    x = re.compile(r"-?\d+")
    numbers = x.findall(string)
    
    if string ==(''):
        return 0      

    neg_list =[]
    for each_number in numbers:
        
        number = int(each_number)
        if number < 0:
            neg_list.append(number)
        elif number <1000:    
            my_sum += number
    if neg_list:
        raise ValueError("negatives not allowed"+str(neg_list))       
    return my_sum 






