def total_squares(n):
    if n == 0:
        return 1
    else:
        return (9 *( 8 ** (n - 1)))

print(total_squares(8))
