
# Declare string with Duplicates(S1,S2)-->Convert to set to remove duplicates-->
#symmetric_difference--> returns all items to result variable except the items on intersection
S1 = "aacdb"
S2 = "gafd"

set1 = set(S1)
set2 = set(S2)
print(set1)
print(set2)


result = set1.symmetric_difference(set2)

#print(list(result))
print(''.join(result))
