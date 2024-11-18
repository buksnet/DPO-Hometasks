import random


def generate_dict(k: int):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = dict()

    for _ in range(k):
        key = random.sample(random.choices(alphabet, k=4), 4)
        value = random.randint(0, 10)
        result.update({''.join(key): value})
    return result


d1, d2 = generate_dict(8), generate_dict(8)
intersect_set = set(map(str, d1.values())) & set(map(str, d2.values()))

modified_dict = dict()

for key, value in d1.items():
    if str(value) in intersect_set:
        modified_dict.update({key: value})

for key, value in d2.items():
    if str(value) in intersect_set:
        modified_dict.update({key: value})

print(modified_dict)