def separate_num(lst):
    numbers = []
   

    for element in lst:
        if str(element).isdigit():
            numbers.append(element)
            

            

    return numbers


a=[1,'a',3,5,6,'w','i','o',1]