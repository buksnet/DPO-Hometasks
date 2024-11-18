import random


def generate_dict(k: int):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = dict()

    for _ in range(k):
        key = random.sample(random.choices(alphabet, k=4), 4)
        value = random.randint(0, 10)
        result.update({''.join(key): value})
    return result


ex = generate_dict(8)
result = list()

for key, value in ex.items():
    keys = list()
    for dkey, dvalue in ex.items():
        if value == dvalue:
            keys.append(dkey)
            if value not in [val[0] for val in result]:
                result.append((value, keys))

print(result)
