def input():
    n = int(input())
    pass
    return number

def search_rate_number(number):
    rate = {}
    for num in number:
        if num in rate:
            rate[num] += 1
        else:
            rate[num] = 1
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


arr = input()
rate = search_rate_number(arr)
min_rate = search_min_rate(rate)
max_number = search_max_number(rate, min_rate)
print(max_number, min_rate)
