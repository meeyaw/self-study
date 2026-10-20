# Study of Insertion Sort
# Sample of Insertion sort with pre-loaded data to sort
# Goal: Sort in Ascending order 


mylist = [64, 34, 25, 12, 2, 11, 999, 5]
n = len(mylist)

for i in range(1,n):
    insert_index = i
    current_value = mylist[i]
    print(f"\ni={i}; Starting list: --> {mylist}")
    print(f"    | Value to sort: mylist[{i}] ==> {current_value}")
    print(f"    | starting insert index:{insert_index}")

    for j in range(i-1, -1, -1):
        print(f"    | j={j}: Is mylist[{j}]={mylist[j]} > mylist[{i}]={current_value}?")
        if mylist[j] > current_value:
            mylist[j+1] = mylist[j]
            insert_index = j
            print(f"    | YES: New insert index:{insert_index}")
        else:
            print(f"    | No: Old insert index:{insert_index}")
            break
    mylist[insert_index] = current_value
    print(f"    | SWAP mylist[{i}] to mylist[{insert_index}]")
    print(f"    ||>> Updated list = {mylist}")

# Final Sorted data
print(f"\nFINAL SORTED LIST: {mylist}\n")
