'''
print("*********** Revome Consecutive Duplicate ******")
string = "soo my naame iss dillip"

# output - "so my name is dilip"

output = ""
temp = ""
for i in string:
    if i != temp:
        output += i
        temp = i

print(temp)
print(output)


print("************** Swap Number ****************")

a = 10
b = 15

a = a + b
b = a - b
a = a - b

print("a :",a, "b: ",b)

print("************** Palindrome **************")

num = int(input())
temp = num
rev = 0
while(num > 0):
    dig = num %10
    rev = rev *10 + dig
    num = num // 10
if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

# print("*************** 3 x 3 Matrix *************")

x,y = map(int,input().split(","))
print(f"*************** {x} x {y} Matrix *************")

lst = []
for i in range(x):
    temp = []
    for j in range(y):
        temp.append(i*j)
    lst.append(temp)
print(lst)

'''
print("********** Finding 3 elements in array given range *********")

array = [0.2,0.3,1.2,0.75,0.8]
a = 1
b = 2

length = len(array)
res = []
for i in range(length-2):
    for j in range(i+1,length-1):
        for k in range(j+1,length):
            temp = []
            total = array[i] + array[j] + array[k]
            if a < total < b:
                temp.append(array[i])
                temp.append(array[j])
                temp.append(array[k])
                res.append(tuple(temp))

print(res)

print("******** OR **********")
from itertools import combinations

def check(val):
    return a < sum(val) < b

lst = list(filter(check,combinations(array,3)))
print(lst)


