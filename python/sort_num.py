def sort_num(lst):
    numbers = []
    for element in lst:
        if str(element).isdigit():
            numbers.append(element)        
    numbers.sort()     
    return numbers


a=[1,'a',3,5,6,'w','i','o',1]
print(sort_num(a))

# Review comment vikas
# Use any mearge sorting algo

