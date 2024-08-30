def binary_search(list,target):
    '''defining the indexes for first and last positions'''
    first = 0 
    last = len(list) - 1
    '''Using a while loop to check the midpoint of list'''
    while first <= last:
        midpoint = (first + last)//2
        '''Using if else to check if midpoint is the target value'''
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target: #if midpoint value is less than target value in the list
            first = midpoint + 1 # we increase the midpoint value
        else:
            last = midpoint - 1 # we decrease the value to get the target value

    return None

#  verify function to check if the target exist in the list    
def verify(index):
    if index is not None:
      print("Target found at index: ", index)
    else:
       print("Target not found in the list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers,12)
verify(result)