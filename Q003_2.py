num_candidates = int(input())
election1 = input().split()
election2 = input().split()

same_votes = []

p = 0


for i in range(len(election1)):
    if election1[p] == election2[p]:
        same_votes.append(str(p + 1))
    p += 1

if len(same_votes) == 0:
    print(0)
else:
    print(" ".join(same_votes))
