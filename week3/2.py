numlist = [12,31,1,23,45,6,3,6,72,4,6,3,7,3,5,6,72,4,5,6]
evensum = 0
for i in numlist:
    if i % 2 == 0:
        evensum += i

print("The sum of all even number: ", evensum)