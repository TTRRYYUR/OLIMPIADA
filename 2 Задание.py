from functools import lru_cache

@lru_cache(maxsize=None)
def min_squares(n):
    if n == 0:
        return 0

    min_count = 5
    i = 1

    while i * i <= n:
        count = 1 + min_squares(n - (i * i))
        if count < min_count:
            min_count = count
        i += 1

    return min_count


n = int(input())
print(min_squares(n))
