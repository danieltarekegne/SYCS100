def bsearch(list,searchvalue):
    low=0                  # low is the index of the first element 
    high=len(list)-1       # high is the index of the last element 
    mid=0                  # mid is the index of the middle element 
    while high>=low:
        mid=(low + high)/2  # mid is the index of midvalue 
        midvalue=list[mid]
        
        if midvalue < searchvalue: # searchvalue is in the upper half of the range
            low=mid+1
        elif midvalue > searchvalue: # searchvalue is in the lower half of the range
            high=mid-1
        else:
            return mid                # return mid index
    return-1                          # searchvalue is not in the range 
