import random
import time
from time import process_time

#The complete Interview Question Code Solution. 

# This is the bubble sort and need to implement the pattern output still...
# Python program for Bubble Sort Interview Question.
  
#Use a function that takes a parameter to be passed to
def bubbleSort(driving_array):
    
    # Get the length of the array item
    n = len(driving_array) 
    
    # Iterate through the item until the end
    for item in range(n-1): 
  
        # Last items are already in place 
        for item2 in range(0, n-item-1): 
  
            # traverse the array from start (0) to n-item-1.
            # Swap if the item is bigger than the next item. 
            if driving_array[item2] > driving_array[item2+1] :
                
                #Switches the order
                driving_array[item2], driving_array[item2+1] = driving_array[item2+1], driving_array[item2] 
  
# test array
#array = [74, 14, 25, 22, 44, 61, 90] 
t1_start = process_time()
input_size = int(input("Please enter size of array: "))
driving_array = [random.randint(1,20000) for i in range(input_size)]


bubbleSort(driving_array)


  
#Prints the sorted array 
print ("Sorted array: ") 
for item in range(len(driving_array)):
    #displays in a column pattern.
    print (driving_array[item], sep=",")
 
t1_stop = process_time() 
print ("the overall time was:",t1_stop -t1_start,"seconds.")






