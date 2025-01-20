TYPE = [
    'Hello',
    int(3),
    3.14,
    [1, 2, 3],
    {1:'Hello', 2: 3, 3: 3.14},
    {1, 2, 3},
    range(1, 10, 1),
    (1, 2, 3),
    True,
]

for i in TYPE :
    print(type(i))
