def recursive_binary_search(list,target):
    #we check if the list is empyty first
    if len(list) == 0:
        return False
    else:
        midpoint = len(list)//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:],target)
            else:
                return recursive_binary_search(list[:midpoint],target)
            
# verify the result
def verify(result):
    print("Targe found: ", result)
    
# numbers = [1,2,3,4,5,6,7,8,9,10]
numbers = []

result = recursive_binary_search(numbers,12)
verify(result)

result = recursive_binary_search(numbers,10)
verify(result)