# Above questions are from 50-interview-questions from bytebybyte

# find the dupes in the given array of elements.
def finddupesinarray():
    l1 = [1,2,1,3,4]
    dupelist = []
    dict = {}
    for item in l1:
        if item not in dict.keys():
            dict[item] = 1
        else:
            dict[item] = dict[item] + 1
    for key in dict.keys():
        print(str(key), ", " + str(dict[key]))
    for key in dict.keys():
        if dict[key] > 1:
            dupelist.append(key)
    print(dupelist)

# find the median of arrays
def medianofarrays():
    arr1 = [1,5,3]
    arr2 = [2,4,6]
    arr1.sort()
    arr2.sort()
    val1 = (arr1[int(len(arr1)/2)])
    val2 = (arr2[int(len(arr2)/2)])
    print(float((val1 + val2)/2))

# Merge K Arrays
def MergeKArrays():
    l1 = [1,5,3]
    l2 = [2,6,5]
    mergedarray = l1 + l2
    mergedarray.sort()
    print(mergedarray)

# Matrix Search
def MatrixSearch():
    lsts = [[1,3],[2,4]]
    target = 2
    for lst in lsts:
        for item in lst:
            if target == item:
                print(True)
            else:
                print(item)
    return False

#BuildOrder
def BuildOrder():
    dict = {0:[], 1:[0], 2:[0], 3:[1,2], 4:[3]}
    lstofbuildorder = []
    for key in dict.keys():
        for values in dict[key]:
            #print(values)
            #for value in values:
            lstofbuildorder.append(values)
        lstofbuildorder.append(key) # to add last project for e.g. 4
    print(set(lstofbuildorder)) # convert to set to remove duplicates and sort.

#Fibonacci
def Fibonacci(n):
    seed = 0
    next = 1
    new = 0
    
    while n-1 >= 1:
        new = seed + next
        seed = next
        next = new
        n = n - 1
    print(new)

# String StringCompression
def StringCompression(s1):
    dict = {}
    compressed = ''
    for ch in s1:
        if ch not in dict.keys():
            dict[ch] = 1
        else:
            dict[ch] = dict[ch] + 1
    for key in dict.keys():
        compressed = compressed + str(key) + str(dict[key])
    print(compressed)

# Kth Most Frequent String
def KthMostFrequentString(strings):
    dict = {}
    for str in strings:
        if str not in dict.keys():
            dict[str] = 1
        else:
            dict[str] = dict[str] + 1
    largestvalue = sorted(dict.values())[-1]
    print(list(dict.keys())[list(dict.values()).index(largestvalue)]) 

#Autocomplete
def Autocomplete():
    set =  {"abc", "acd", "bcd", "def", "a", "aba"}
    prefix = 'b'
    l = []
    for each in set:
        if prefix in each[0]:
            l.append(each)
    print(l)

#Swap SwapVariables
def SwapVariables():
    var1 = 10
    var2 = 20
    print("values before swap:" + str(var1)+ "," + str(var2))
    var1 = var1 + var2
    var2 = var1 - var2
    var1 = var1 - var2
    print("values after swap:" + str(var1)+ "," + str(var2))

# PalendromesForGivenList
def PalendromesForGivenList():
    l1 = [1,2,2,1]
    l2 = l1[::-1] # to reverse the list.
    print("Given list is: " + str(l1))
    if (l1 == l2):
        print("Given list is a palendrome")
    else:
        print("Given list is NOT a palendrome")

# FindTwoMissingNumbers.. from given 1..n numbers in sequence
def FindTwoMissingNumbers():
    l1 = [1,3,5]
    missing_l1 = []
    dict = {}
    sum = 0
    sum_list = 0
    for each in range(5):
        if each not in l1:
            dict[each] = 0
        else:
            dict[each] = each
    for key in dict.keys():
        if dict[key] == 0:
            missing_l1.append(key)
    print(missing_l1)

# Smallest Change - find min coins needed to make up the Change
def SmallestChange():
    number_coins = 0
    remaining_change = 0
    change = 76
    while change > 0:
        if change > 25:
            number_coins = number_coins + change/25
            remaining_change = change%25
            change = remaining_change
        elif change > 10:
            number_coins = number_coins + change/10
            remaining_change = change%10
            change = remaining_change
        elif change > 5:
            number_coins = number_coins + change/5
            remaining_change = change%5
            change = remaining_change
        elif change >= 1:
            number_coins = number_coins + change/1
            remaining_change = change%1
            change = remaining_change
    print("total number of coins needed:", number_coins)

# Zero Sum Subarray
def ZeroSumSubarray():
    l1 = [1, 2, -5, 1, 2, -1]
    sub_list = []
    first_index = 0
    second_index = 0
    main_index = 0
    for first_index in range(len(l1)-1):
        second_index = 0
        sub_list = []
        print("**")
        for second_index in range(first_index + 1):
            sub_list.append(l1[second_index])
            print(str(second_index) + "," + str(l1[second_index]))
        if sum(sub_list) == 0:
            print(sub_list)

# FactorialOfANumber recursively
def FactorialOfANumberRecursively(n):
    if n > 1:
        return n * FactorialOfANumberRecursively(n-1)
    else:
        return 1
        
# FactorialOfANumber with a loop
def FactorialOfANumberLoop(n):
    factorial = 1
    while n > 1:
        factorial = factorial * n
        n = n - 1
    return factorial

#print("Factorial of a number with loop:" + str(FactorialOfANumberLoop(5)))
print("Factorial of a number recursively:" + str(FactorialOfANumberRecursively(7)))

ZeroSumSubarray()

# SmallestChange()
# FindTwoMissingNumbers()
# PalendromesForGivenList()
# SwapVariables()

# Autocomplete()
# KthMostFrequentString({"a","b","c","a","b","a"}) # most occuring.
# StringCompression("aaabbbcddd")
# Fibonacci(5)

# BuildOrder()  
# MatrixSearch()  
# MergeKArrays()
# medianofarrays()
# finddupesinarray()

