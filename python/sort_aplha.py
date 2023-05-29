def bub_sort(arr):
    n=len(arr)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if arr[j+1]<a[j]:
                arr[j+1],a[j]=a[j],a[j+1]
    return arr
def sort_alpha(lst):
    alphabets = [] 
    for element in lst:
        if (str(element).isalpha()):
           alphabets.append(element)
     
    return  alphabets
a=[1,'a',3,5,6,'w','i','o',1]
sort_alpha(a)
bub_sort(a)
# Review comment vikas
# Use any bubble sorting algo


    