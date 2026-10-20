# Study of Selection Sort
# Sample of selection sort with pre-loaded data to sort
# Goal: Sort in Ascending order
# 
# Selection Sort flow:
# 1. Go through the array to find the lowest value.
# 2. Move the lowest value to the front of the unsorted part of the array.
# 3. Go through the array again as many times as there are values in the array.
# 
# Implementation:
# 1. Set two loops -- Outer loop (i) and inner loop (j). 
#    Outer loop controls how many times the inner loop must run. For a list of n elements, this outer loop
#        will run n-1 times. 
#    Inner loop is the one that goes through the elements of the list, find the lowest value, then move 
#        it on front. This loop will loop through one less value each time it runs
# 2. Run this script to see the detailed explanation how sorting goes

mylist = [64, 34, 25, 12, 2, 11, 999, 5]
n = len(mylist)

for i in range(n):
    print(f"\ni={i}; Starting list: --> {mylist}")
    min_index = i
    print(f"    | starting min index:{min_index}\tmylist[{min_index}] ==> {mylist[min_index]}")
    print(f"    *")
    for j in range(i+1, n):
         print(f"    | j={j}: Is {mylist[j]} < {mylist[min_index]}?")
         if mylist[j] < mylist[min_index]:
             min_index = j
             print(f"    | YES: New min index:{min_index}\tmylist[{min_index}] ==> {mylist[min_index]}")
             print(f"    *")
         else:
             print(f"    | NO: Old min index:{min_index}\tmylist[{min_index}] ==> {mylist[min_index]}")
             print(f"    *")

    mylist[i], mylist[min_index] = mylist[min_index], mylist[i]
    print(f"    | SWAP mylist[{min_index}] to mylist[{i}]")
    print(f"    ||>> Updated list = {mylist}")

# Final Sorted data
print(f"\nFINAL SORTED LIST: {mylist}\n")