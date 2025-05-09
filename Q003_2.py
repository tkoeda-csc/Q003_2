num_candidates = int(input())
election1 = input().split()
election2 = input().split()

same_votes = []


for i in range(len(election1)):
    if election1[i] == election2[i]:
        same_votes.append(str(i + 1))

if len(same_votes) == 0:
    print(0)
else:
    print(" ".join(same_votes))
