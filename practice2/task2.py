import random


def generate_list(k):
    return [random.randrange(0, 10) for _ in range(k)]


l1, l2 = generate_list(8), generate_list(8)
l3 = list()

l3 += l1[::2] + l2[0::2]

print(l3)
