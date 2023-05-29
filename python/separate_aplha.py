def separate_alpha(lst):
    alphabets = []
     
    for element in lst:
        if (str(element).isalpha()):
           alphabets.append(element)
            
   

    return  alphabets
a=[1,'a',3,5,6,'w','i','o',1]
print(separate_alpha(a))
