def batched(iterable, n):
    for i in range(0, len(iterable), n):
        yield tuple(iterable[i:i + n])

numbers = [1, 2, 3, 4, 56, 6, 6, 7, 8, 8, 7654, 998, 6, 7, 8, 7, 654, 3, 978, 5, 6, 7, 90]

print(type(numbers))

batches = batched(numbers, 3)
print("Batched list (size 3):", list(batches))
