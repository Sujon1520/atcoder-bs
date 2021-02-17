# ABC087B Coins

a = int(input())  #number of 500yen coin
b = int(input())  #100yen
c = int(input())  #50yen
x = int(input())  #Total amount
num_combination = 0
for n500 in range(0,a+1):
    for n100 in range(0, b+1):
        for n50 in range(0,c+1):
            amount = 500*n500+100*n100+50*n50
            # print(n500, n100, n50, amount)
            if amount == x:
                num_combination += 1

print(num_combination)