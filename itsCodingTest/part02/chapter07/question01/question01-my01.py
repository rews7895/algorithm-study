n = 5
all_parts = [8, 3, 7, 9, 2]
m = 3
request_parts = [5, 7, 9]

all_parts.sort()

for request_part in request_parts:
    result = None
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2
        if all_parts[mid] == request_part:
            result = mid
            break
        elif all_parts[mid] > request_part:
            end = mid - 1
        else:
            start = mid + 1

    if result is None:
        print('no', end=' ')
    else:
        print('yes', end=' ')
