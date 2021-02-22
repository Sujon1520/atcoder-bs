# atcoder ABC088B card game for two

N = int(input())
cards = list(map(int, input().split()))
cards.sort(reverse=True)

alice = 0
bob = 0

for i in range(N):
    if i % 2 == 0:
        alice += cards[i - 1]
    else :
        bob += cards[i - 1]

print(alice-bob)
