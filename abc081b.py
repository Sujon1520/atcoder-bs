'''
s = input()
token = s.split()

num_list = []  # empty list
while token:
    num_list.append(int(token.pop(0))  #take 1st element and convert to int
'''
size = int(input())
num_list = list(map(int, input().split()))

num_div = 0
while True:
    for i in range(size):
        if num_list[i]%2 == 1:
            all_even = False
            break
        else:
            num_list[i] //=2
    if all_even:
        num_div += 1
print(num_div)