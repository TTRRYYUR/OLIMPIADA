def input_list():
    n = int(input())
    numbers = []

    
    while len(numbers) < n:
        line_numbers = list(map(int, input().split()))
        for num in line_numbers:
            numbers.append(num)
    return numbers


def search_rate_number(numbers):
    rate = {}
    for num in number:
        rate[num] = rate.get(num, 0) + 1
    return rate


def search_min_rate(rate):
    minimum_rate = min(rate.values())
    return minimum_rate


def search_max_number(rate, min_rate_number):
    max_number = []
    for number, count in rate.items():
        if count == min_rate_number:
            max_number.append(number)
    return max(max_number)


arr = input_list()
rate = search_rate_number(arr)
min_rate = search_min_rate(rate)
max_number = search_max_number(rate, min_rate)
print(max_number, min_rate)
