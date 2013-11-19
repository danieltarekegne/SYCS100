

def bsearch(list,searchvalue):
    
    low=0
    high=len(list)-1
    mid=0
    while high>=low:             
        mid=(low + high)/2       # midvalue position
        midvalue=list[mid]
        
        if midvalue < searchvalue:  # searchvalue is in the upper half of the range
            low=mid+1
        elif midvalue > searchvalue: # searchvalue is in the lower half of the range
            high=mid-1
        else:
            return mid               # return mid index
            
    return-1                         # searchvalue is not in the range

   
