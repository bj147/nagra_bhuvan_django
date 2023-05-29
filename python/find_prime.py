def prime_num(lst):
    numbers = []
    prime=[]
    nonprime=[]

    for element in lst:
        if str(element).isdigit():
            numbers.append(element)
            
    for nums in numbers:
        if(nums==1 ):
            prime.append(1)
        elif(nums==2):
            prime.append(2)         
        else:    
            for i in range(2,int(nums)) :
                if nums%i==0:
                    nonprime.append(nums)
                    break
                else:
                    prime.append(nums)
                    break
    return prime


a=[1,'a',3,5,6,'w','i','o',11]
print(a)

# Review comment vikas
# use recurction
