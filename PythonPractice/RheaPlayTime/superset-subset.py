
# this question was asked by Okta HM. 
sp = {1, 2, 3, 4, 5, 6}

# 2s set
# (1,2), (1,3), (1, 4), ....(5,6)
# 3s set = 1st set of previous set + 2nd element of remaining set.
# (1,2,3), (1,2,4), (1,2,5), (1,2,6), (1,3,4)...
# 4s set = 1st set of previous set + 3rd element of remaiing set
# (1,2,3,4), (1,2,3,5), (1,2,3,6), (1,2,4,5), (1,2,4,6) ...
print("Given super set:" + str(sp))
s2 = set()
for each in sp:
    plusOne = each + 1
    for plusOne in sp:
        if each < plusOne:
            tuple1 = (each, plusOne)
            s2.add(tuple1)
print("lengh of 2s sub-set: " + str(len(s2)))
l1 = list(s2)
l1.sort()
print(str(l1))

#s2 = tuple(sp)
counter = 2
while counter < len(sp):
#convert set s2 to list to be able to index
    s3 = set()
    l2 = list(s2)
    for each in range(len(l2)):
        plusTwo = each + 1
        for plusTwo in range(len(l2)):
            # todo: figure out the len on single element tuple.
            lastnumberindex_in_1stset = len(l2[0]) - 1
            if l2[each][lastnumberindex_in_1stset] < l2[plusTwo][lastnumberindex_in_1stset]:
            #if l2[each][1] < l2[plusTwo][1]:
                temp_list_and_convert_tuple = []
                for index in range(len(l2[0])):
                    temp_list_and_convert_tuple.append(l2[each][index])
                    if index == len(l2[0]) - 1:
                        temp_list_and_convert_tuple.append(l2[plusTwo][index])
                tuple2 = tuple(temp_list_and_convert_tuple)
                #tuple2 = (l2[each][0], l2[each][1], l2[plusTwo][1])
                s3.add(tuple2)
    print("lengh of " + str(counter + 1) + "s sub-set: " + str(len(s3)))
    l3 = list(s3)
    l3.sort()
    print(str(l3))
    s2 = s3
    counter = counter + 1
