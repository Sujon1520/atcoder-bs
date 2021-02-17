# ABC087B Coins

a = int(input())  #number of 500yen coin
b = int(input())  #100yen
c = int(input())  #50yen
x = int(input())  #Total amount
num_combination = 0
for n500 in range(0,a+1):
    for n100 in range(0, b+1):
        n50 = (x - n500*500 - n100*100) // 50
        if n50 <= c and n50>=0:
            num_combination += 1

print(num_combination)