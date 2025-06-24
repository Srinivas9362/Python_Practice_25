numbers = [1,1,6,9,8,8,2,3,4,5,5,6,3,4,7,1]

print(numbers)

#1st method to remove duplicates via tuples as it won't store the duplicates

print("The excluded duplicates are :",list(set(numbers)))

#2nd method to remove duplicates via dictionary as it won't store the duplicates

print("The final list after removing the duplicates are: ",list(dict.fromkeys(numbers)))


# print("The dictnary of the numbers are: ",dict(numbers))

from collections import Counter
print("Count of each number:", dict(Counter(numbers)))


count_dict = {}
for i in numbers:
    if i in count_dict:
        count_dict[i] += 1
    else:
        count_dict[i] = 1

for key in count_dict:
    print(f"Number {key} occurs {count_dict[key]} time(s)")

print(count_dict.keys())
print(count_dict.values())
print(count_dict)



sorted_by_keys = dict(sorted(count_dict.items()))
print("Sorted by keys:", sorted_by_keys)

