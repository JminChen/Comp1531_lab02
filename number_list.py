def find_reverse(numbers):
    #TODO: find the reverse of the list
    return list(reversed(numbers))


def find_max(numbers):
    #TODO: find the maximum of the list
    return max(numbers)
        
def find_min(numbers):
    #TODO: find the minimum of the list
    return min(numbers)

def find_sum(numbers):
    #TODO: find the sum of all the numbers in the list
    return sum(numbers)

def find_average(numbers):
    #TODO: find the average of all the numbers in the list
    return sum(numbers)/len(numbers)

def find_descending(numbers):
    #TODO: numbers sorted in descending order
    return sorted(numbers,reverse=True)

def second_smallest(numbers):
    #TODO: find the second smallest
    
    ascending_list = sorted(numbers)
    
    for x in ascending_list:
        if x > min(numbers):
            return x
           


'''
 bonus task:
 a function that takes in a list of numbers, and an index 'k' 
 and prints the kth smallest number in the list
'''
def kth_smallest(numbers, k):
    #TODO: find the kth smallest number in the list
    return sorted(set(numbers))[k - 1]

