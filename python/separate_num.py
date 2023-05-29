import pdb
def separate_num(lst):
    numbers = []
    for element in lst:
        if (str(element).isdigit()):
            numbers.append(element)           
    return numbers
a=[1,'a',3,5,6,'w','i','o',1]
print(separate_num(a))
# Review Comment Vikas
# try with NAN
# import pdb
# pdb.set_trace()
def separate_num(lst):
    numbers = []
    pdb.set_trace()
    for element in lst:
        if (str(element).isdigit()):
            numbers.append(element)           
    return numbers