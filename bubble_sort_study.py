# Study of how bubble sort happens
# Sample of bubble sort with pre-loaded data to sort
# Goal: Sort in Ascending order

# example list:
mylist = [64, 34, 25, 12, 2, 11, 999, 5]
n = len(mylist)
print(f"\nList Length = {n}")

for i in range(n-1):
     print(f"\nStarting list: --> {mylist}")

     # Last i elements are already in place; no need to check them
     for j in range (n-i-1):
            print(f"i[{i}] ==> {mylist[i]}   j[{j}] ==> {mylist[j]}   j[{j+1}] ==> {mylist[j+1]}")
            print(f"    | Compare: Is {mylist[j]} > {mylist[j+1]} ?")
            if mylist[j] > mylist[j+1]:                             # This checks the adjacent numbers
                  mylist[j], mylist[j+1] = mylist[j+1], mylist[j]   # This is where swapping happens
                  print(f"    | SWAP: --> {mylist}")
            else:
                  print(f"    | NO SWAP: --> {mylist}")
                  
# Final Sorted data
print(f"\nFINAL SORTED LIST: {mylist}\n")




                  




