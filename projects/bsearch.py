list=[22,36,43,55,64,77,80,88]



def bsearch(list,searchvalue):
    
    low=0
    high=len(list)-1
    mid=0
    while high>=low:
        mid=(low + high)/2
        midvalue=list[mid]
        
        if midvalue < searchvalue:
            low=mid+1
        elif midvalue > searchvalue:
            high=mid-1
        else:
            return mid
    return-1
print bsearch (list,77) 
