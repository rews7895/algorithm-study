n, m = 4, 6
length_list = [19, 15, 10, 17]

result = None
start = 0
end = max(length_list)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in length_list:
        if i > mid:
            total += i - mid

    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
