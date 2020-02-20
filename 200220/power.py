# for count in [(10**5),(9**5),(8**5),(7**5),
# (6**5),(5**5),(4**5),(3**5),(2**5),(1**5)] :
#     print(count)
counter = 1
while(counter < 11):
    print(counter ** 5)
    counter = counter + 1

# countArr = [2,3,4,5,6,7,8,9,10,11]
countArr = range(10)

for count in countArr :
    print((count)**5)
