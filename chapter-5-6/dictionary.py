obj = {
    'a': 1,
    'b': 2,
    'c d': 4,
    (1, 2): 5
}

# obj.update({ 'c': 2 })
# obj['c'] = 3

# obj.setdefault('c', 3)
#
# print(obj)

for key, val in obj.items():
    print(key, val)