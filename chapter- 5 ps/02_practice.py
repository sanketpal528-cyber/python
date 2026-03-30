num = []
for i in range(8):
    n = int(input("enter a number: "))
    num.append(n)
    unique_num = list(set(num))
    print("unique numbers:", unique_num)
# # set is a collection of unique elements. It is unordered and unindexed. It is mutable but does not allow duplicate values. It is defined by using curly braces {} or by using the set() function.