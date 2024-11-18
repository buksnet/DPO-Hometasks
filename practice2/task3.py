import random


def generate_list(k):
    return [random.randrange(0, 10) for _ in range(k)]


l1 = list(map(str, generate_list(8)))

for i, v1 in enumerate(l1):
    for j, v2 in enumerate(l1[i+1:]):
        if v1 == v2:
            del l1[j]
print(l1)
