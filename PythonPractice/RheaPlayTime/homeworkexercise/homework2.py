# length of list
thinkofaname = ['banana', 'lamp', 'mold', 'rust']
print(type(thinkofaname))
print(len(thinkofaname))
thunkofaname = [3, 4, 5, 2, 7, 19]
print(type(thunkofaname))
thisisthesizeofthelist = "This is the size of the list"
print(thisisthesizeofthelist + ':' + str(len(thunkofaname)))
t = 'This is my list:'
print(t + str(thunkofaname))

#This below program is to print all the numbers in a given list
# and also add all the numbers and print the total.
sum1 = 0
#This code below is a counter that stores the integer 0
counter = 0
#This code stores a list containing 4 integers
lista = [1, 3, 1, 4, 6, 10, 31, 9, 12, 12, 11, 13,
1, 3, 1, 4, 6, 10, 31, 9, 12, 12, 11, 13,
1, 3, 1, 4, 6, 10, 31, 9, 12, 12, 11, 13,
1, 3, 1, 4, 6, 10, 31, 9, 12, 12, 11, 13,
1, 3, 1, 4, 6, 10, 31, 9, 12, 12, 11, 13,
1, 3, 1, 4, 6, 10, 31, 9, 12, 12, 11, 13,
1, 3, 1, 4, 6, 10, 31, 9, 12, 12, 11, 13,
1, 3, 1, 4, 6, 10, 31, 9, 12, 12, 11, 13,
1, 3, 1, 4, 6, 10, 31, 9, 12, 12, 11, 13,
1, 3, 1, 4, 6, 10, 31, 9, 12, 12, 11, 13,
1, 3, 1, 4, 6, 10, 31, 9, 12, 12, 11, 13,
1, 3, 1, 4, 6, 10, 31, 9, 12, 12, 11, 13,
1, 3, 1, 4, 6, 10, 31, 9, 12, 12, 11, 13,
1, 3, 1, 4, 6, 10, 31, 9, 12, 12, 11, 13]
#This is a while loop
while True:
    #This will print the current counter value as an index in lista
    print(lista[counter])
    #This code below is where we add 1 more to the counter to keep it going 
    counter = (counter)
    sum1 = (sum1 + (lista[counter])) 
    counter = (counter + 1)
    #This is where we see if the counter is equal to 4 if it is we stop the loop
    if counter == len(lista):
        break
print("The total equals to:" + str(sum1))


## Print true if 2 given integer are same else false.
while True:
    Int1 = input("Which number do you choose:")
    Int2 = input("What other number do you choose:")
    Int3 = input("What is the third number you choose:")
    if Int1 == Int2 == Int3:
        print("true")
    else:
        print("false")
    if Int1 == Int2 or Int1 == Int3
        print(Int1)
    if Int2 == Int3 or Int2 == Int1:
        print(Int2)
    if Int1 <> Int3 <> Int2:
        print("None of the numbers you chose match your other numbers")
